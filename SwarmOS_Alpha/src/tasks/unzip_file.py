# src/tasks/unzip_file.py
import zipfile
import os

def run(args):
    if len(args) < 2:
        return "Usage: unzip_file <input.zip> <output_folder>"

    zip_path, output_dir = args

    if not os.path.exists(zip_path):
        return f"Zip file '{zip_path}' not found."

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        return f"✅ Unzipped '{zip_path}' into '{output_dir}'"
    except Exception as e:
        return f"Unzip error: {e}"
