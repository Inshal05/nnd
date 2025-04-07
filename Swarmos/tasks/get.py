import os

async def run(payload):
    filename = payload.get("filename")
    path = os.path.join("storage/incoming", filename)
    
    if not os.path.exists(path):
        return {"error": "File not found"}

    with open(path, "r") as f:
        data = f.read()
    
    return {"data": data}
