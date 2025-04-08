import psutil

def perform(payload):
    memory = psutil.virtual_memory()
    return {
        "memory_percent": memory.percent,
        "available": memory.available
    }
