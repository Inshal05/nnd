import os

def init_storage():
    dirs = [
        "storage/incoming",
        "storage/decrypted",
        "storage/unzipped",
        "storage/temp"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
