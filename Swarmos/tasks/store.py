import os

async def run(payload):
    filename = payload.get("filename")
    data = payload.get("data")

    if not filename or not data:
        return {"error": "Missing filename or data"}

    path = os.path.join("storage/incoming", filename)
    with open(path, "w") as f:
        f.write(data)
    
    return {"status": "stored", "path": path}
