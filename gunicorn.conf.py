import os

# Render dynamic port binding
port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

# Optimized concurrency for cloud containers (prevents lockups)
workers = 1
threads = 4
worker_class = "gthread"
timeout = 120
keepalive = 5

# Logging to stdout for Render Live Logs
accesslog = "-"
errorlog = "-"
loglevel = "info"
