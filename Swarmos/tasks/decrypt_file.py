from utils.encryption import decrypt_data
import os

async def run(payload):
    filename = payload.get("filename")
    key = payload.get("key")

    path = os.path.join("storage/incoming", filename)
    if not os.path.exists(path):
        return {"error": "File not found"}

    with open(path, "rb") as f:
        encrypted = f.read()
    
    decrypted = decrypt_data(encrypted, key)

    out_path = os.path.join("storage/decrypted", f"decrypted_{filename}")
    with open(out_path, "wb") as f:
        f.write(decrypted)

    return {"status": "decrypted", "path": out_path}
