# src/tasks/status.py
import psutil

def run(args):
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return (
        f"🧠 CPU Usage: {cpu}%\n"
        f"💾 Memory: {mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB ({mem.percent}%)\n"
        f"📁 Disk: {disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB ({disk.percent}%)"
    )
