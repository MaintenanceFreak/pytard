# pytard (*π-tard*)

```
     _________   _                _ 
    |_________| | |_ __ _ _ __ __| |
      | | | |   | __/ _` | '__/ _` |
      | | | |   | || (_| | | | (_| |
      |_| |_|    \__\__,_|_|  \__,_|

```

Slowly serve 42,069 digits of π for dumb bots and wannabe hackers poking around where they don’t belong.

---

![π-tard](https://img.shields.io/badge/π--tard-contributor-brightgreen)

**π-tard** is a passive-aggressive application-layer honeypot that serves  
**42,069 digits of π**, one byte every 4.9 seconds.

## Why?
Bots keep trying to steal `.env` files from our servers.  
We could have simply blocked them, but that would be boring.  
Instead, we chose violence, and long-term entertainment.

To be fair, whoever wrote the bot had just enough brain cells to write a working script.  
So it felt only right to reward their effort — with 42,069 digits of π, one byte at a time.  

Why let them scan endpoint after endpoint when we can save them the trouble  
and give them exactly what they want… on our terms?  

And hey, they showed up.  
They deserve recognition.  

So we built them a leaderboard.

## How it works:
- HTTP server accepts connection
- Sends `200 OK` with keep-alive
- Drips one digit of pi every 4.9s
- Logs their IP, headers, and ragequit point
- Posts high scores a leaderboard log file
- Ties up scanners for hours or days, preventing them from hitting other targets
- Async and non-blocking — can handle thousands of simultaneous connections
- Memory usage is negligible; CPU barely notices
- Comes with clean logging and optional leaderboard path customization

## Install
No PyPI. No bs. Just drop the file and run it.

1. Clone the repo
```sh
git clone https://github.com/MaintenanceFreak/pytard.git
cd pytard
```

2. Run the server
```sh
python3 pytard.py -h
```

### Optional: 

#### Systemd Service
Want it to run on boot like a proper menace?  
A sample service file is included:  
```sh
sudo cp templates/pytard.service /etc/systemd/system/pytard.service
sudo systemctl daemon-reexec
sudo systemctl enable --now pytard.service
```
Edit the ExecStart path in the .service file if you moved the script.

#### Apache Tarpit Redirect
Want to forward bots to the tarpit via Apache?  
Use the provided pytard.httpd.conf snippet to route .env or unwanted paths directly to the pain server:  
```sh
sudo cp templates/pytard.httpd.conf /etc/httpd/conf.d/pytard.conf
sudo systemctl reload httpd
```
Make sure Apache is set to forward to localhost:42069, or whatever port you're using.

### Recommended: System Tuning (for max pain output)
Want to hold thousands of bots hostage without breaking a sweat?  
Apply the kernel and ulimit tweaks in the fine_tuning folder.  
> - We currently only have one for linux (AL9 / RHEL9)

## Usage
```sh
usage: pytard.py [-h] [--log-path LOG_PATH] [--leaderboard-path LEADERBOARD_PATH]

pytard – Tarpit for .env thieves, serves pi

optional arguments:
  -h, --help            show this help message and exit
  --log-path LOG_PATH   Path to activity log file
  --leaderboard-path LEADERBOARD_PATH
                        Path to leaderboard log file
```

## 🏆 Our Current Record Holder (As of 06-03-2025)
> 34 hours.  
> ~25,000 digits.  
>  
> We salute your suffering, little bot.

## Live Demo 🧪
Think you’re slick?  
Try to steal our secrets at  
👉 [https://maintenancefreak.com](https://maintenancefreak.com)  

Good luck.  
There's a leaderboard.

## Contribution 
This project wasn’t built out of necessity.  
It was built out of spite, boredom, and a love for dumb ideas done well.  

Got something to add?  
>    - Want to host a public leaderboard? Do it. We'll link it.  
>    - Make a Grafana dashboard with bot stats? Hell yes — we’ll use it.  
>    - New torture formats? Hex dump, Morse, Base64, Goatse-in-ASCII? Chef’s kiss.
>    - Better ascii art pi symbol for our readme? We'll use it and give you a shoutout.

Fork it, break it, make it funnier, make it worse — make it yours. Enjoy.  

💌 PRs welcome.  
🧠 Bonus points if it’s funny and makes someone’s server cry.  
🏆 Top-tier absurdity gets you a free 1-year Premium subscription to MaintenanceFreak when we launch.  

Earn it with chaos.

Our secrets were never in danger.  
We just got bored reading the logs.  

They came looking for our goods, so we gave them some delicious π.  

Because if you're going to knock on our door uninvited,  
you better be ready for what's on the other side:  
spite, sarcasm, and a mathematically precise middle finger.
