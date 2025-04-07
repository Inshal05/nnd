import os
import zipfile

async def run(payload):
    filename = payload.get("filename")
    path = os.path.join("storage/incoming", filename)

    if not os.path.exists(path):
        return {"error": "ZIP file not found"}

    out_dir = os.path.join("storage/unzipped", filename.replace(".zip", ""))
    os.makedirs(out_dir, exist_ok=True)

    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(out_dir)

    return {"status": "unzipped", "path": out_dir}
