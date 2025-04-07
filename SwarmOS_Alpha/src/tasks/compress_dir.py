# src/tasks/compress_dir.py
import shutil

def run(args):
    if len(args) < 2:
        return "Usage: compress_dir <folder> <output.zip>"
    folder, output_zip = args
    try:
        shutil.make_archive(output_zip.replace('.zip', ''), 'zip', folder)
        return f"Folder {folder} compressed to {output_zip}"
    except Exception as e:
        return f"Compression error: {e}"
