# 🧠 System Tuning for Maximum Pain Delivery
To fully unleash π-tard and serve 42,069 digits of delicious π to thousands of bots simultaneously, your system needs to be tuned for high socket concurrency and low I/O bottlenecks.
Apply the following changes to maximize open file descriptors, TCP queue sizes, and socket reuse efficiency:


```bash
# Edit /etc/sysctl.conf or run:
sysctl -w net.core.somaxconn=65535
sysctl -w net.ipv4.tcp_tw_reuse=1
sysctl -w net.ipv4.tcp_max_syn_backlog=65535
sysctl -w net.ipv4.ip_local_port_range="1024 65535"
```

```md
# Edit /etc/security/limits.conf
* soft nofile 65535
* hard nofile 65535
```

```bash
# Apply immediately in your shell session
ulimit -n 65535
```

🧪 What this gives you:
- Tens of thousands of concurrent bot sockets
- Each bot gets slow-dripped pi
- You keep your CPU happy
- Logs or telemetry can be added without blocking

Result:
Bots get stuck in a mathematically torturous purgatory,
you get performance, control, and something fun to look at when you're tired of being productive.