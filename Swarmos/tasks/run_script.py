import subprocess

async def handle(data):
    script_path = data.get("path")
    try:
        output = subprocess.check_output(["python", script_path], stderr=subprocess.STDOUT)
        return output.decode()
    except Exception as e:
        return str(e)
