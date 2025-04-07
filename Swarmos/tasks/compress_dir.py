import shutil

async def handle(data):
    folder = data.get("folder")
    output = data.get("output", folder + ".zip")
    shutil.make_archive(folder, 'zip', folder)
    return f"Compressed into {output}"
