import zipfile
import os

def perform(payload):
    filename = payload.get("filename")

    if not filename or not os.path.exists(filename):
        return {"error": "File not found or filename missing"}

    zip_filename = filename + ".zip"

    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(filename, arcname=os.path.basename(filename))
        return {"result": f"Zipped successfully as {zip_filename}"}
    except Exception as e:
        return {"error": str(e)}
