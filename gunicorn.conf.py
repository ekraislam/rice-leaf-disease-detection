import os

# Render dynamic port binding
port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

# ── Worker Configuration ───────────────────────────────────────────────────────
# 1 worker + 4 threads is optimal for Render free tier (0.1–0.5 vCPU shared).
# gthread lets multiple requests be handled concurrently without spawning
# extra OS processes (which would clone the model into memory again).
workers = 1
threads = 4
worker_class = "gthread"

# ── Timeouts ──────────────────────────────────────────────────────────────────
timeout = 120          # kill worker if request takes > 120s
graceful_timeout = 30  # time for worker to finish current requests on reload
keepalive = 30         # keep idle HTTP connections open 30s
                       # reduces TCP handshake overhead on repeated requests

# ── PyTorch OpenMP Safety: preload_app = False ──────────────────────────────
# In PyTorch on Linux, loading the model in the master process before forking
# can cause OpenMP threadpool deadlocks/crashes. Setting preload_app = False
# ensures clean, safe model initialization per worker.
preload_app = False

# ── Memory Management ─────────────────────────────────────────────────────────
# Restart worker after N requests to prevent slow memory creep.
max_requests = 500
max_requests_jitter = 50  # randomize to avoid all workers restarting at once

# ── Logging to stdout for Render Live Logs ────────────────────────────────────
accesslog = "-"
errorlog = "-"
loglevel = "info"
