import zipfile
import os

def perform(payload):
    filename = payload.get("filename")
    if not filename:
        return {"error": "Missing filename"}

    try:
        with zipfile.ZipFile(os.path.join("storage", filename), 'r') as zip_ref:
            zip_ref.extractall("temp")
        return {"message": f"{filename} unzipped to temp/"}
    except Exception as e:
        return {"error": str(e)}
