import os

def perform(payload):
    filename = payload.get("filename")
    content = payload.get("file_content")

    if not filename or content is None:
        return {"error": "Missing filename or data"}

    filepath = os.path.join("storage", filename)
    with open(filepath, "w") as f:
        f.write(content)
    return {"message": f"File '{filename}' saved successfully."}
