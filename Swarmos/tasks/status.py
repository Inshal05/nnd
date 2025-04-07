import psutil

async def run(payload):
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    return {
        "cpu_usage": cpu,
        "available_memory": memory.available // 1024,
        "total_memory": memory.total // 1024
    }
