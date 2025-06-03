#!/usr/bin/env python3
import asyncio
import argparse
import os
from datetime import datetime
from mpmath import mp

mp.dps = 42070
PI_DIGITS = str(mp.pi)[:42069]
PORT = 42069

LEADERBOARD = "/var/log/pytard/leaderboard.log"
LOG_PATH = "/var/log/pytard/activity.log"

def set_log_path(path):
    global LOG_PATH
    LOG_PATH = path
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def set_leaderboard_path(path="/var/log/pytard/leaderboard.log"):
    global LEADERBOARD
    LEADERBOARD = path
    os.makedirs(os.path.dirname(LEADERBOARD), exist_ok=True)


def log_loser(addr, headers):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOG_PATH, "a") as f:
        f.write(f"\n📜 Logging loser: {addr}\n")
        f.write(f"[{timestamp}] Connection from {addr[0]}:{addr[1]}\n")
        for line in headers:
            f.write(f"  {line}\n")
        f.write("\n")


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    start_time = datetime.utcnow()
    digit_index = 0

    try:
        data = await asyncio.wait_for(reader.readuntil(b"\r\n\r\n"), timeout=5)
        headers = data.decode(errors="ignore").split("\r\n")

        writer.write(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain\r\n"
            b"Connection: keep-alive\r\n\r\n"
        )
        await writer.drain()

        log_loser(addr, headers)

        user = "Unknown"
        for line in headers:
            if line.startswith("X-Forwarded-For:"):
                user = line.split(":", 1)[1].strip()
                break

        with open(LEADERBOARD, "a") as f:
            f.write(f"User: {user} | Begin Challenge | Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

        print(f"🎯 Caught one: {addr}")

        for char in PI_DIGITS:
            try:
                writer.write(char.encode())
                await writer.drain()
                digit_index += 1
                await asyncio.sleep(4.9)
            except Exception:
                break

        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()
        with open(LEADERBOARD, "a") as f:
            if digit_index < 42069:
                f.write(f"User: {user} | Status: Failure | Disconnected early at {digit_index} digits of pi. | Total time: {duration:.2f} seconds\n")
            else:
                f.write(f"User: {user} | Status: WINNER | Completed the challenge of reaching {digit_index} digits of pi! | Total time: {duration:.2f} seconds\n")
            f.write(f"User: {user} | End | End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

    except Exception:
        pass
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, "0.0.0.0", PORT)
    print(f"🌘 Tarpit listening on port {PORT}...")
    async with server:
        await server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(description="πtard – Tarpit for .env thieves")
    parser.add_argument(
        "--log-path", default="/var/log/pytard/activity.log",
        help="Path to activity log file"
    )
    parser.add_argument(
        "--leaderboard-path", default="/var/log/pytard/leaderboard.log",
        help="Path to leaderboard log file"
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # Set log paths
    set_log_path(args.log_path)
    set_leaderboard_path(args.leaderboard_path)

    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass
    asyncio.run(main())
