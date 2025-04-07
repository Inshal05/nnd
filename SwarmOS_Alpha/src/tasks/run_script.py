# src/tasks/run_script.py
import subprocess

def run(args):
    if len(args) < 1:
        return "Usage: run_script <script.py>"
    try:
        result = subprocess.run(["python"] + args, capture_output=True, text=True)
        return f"Script Output:\n{result.stdout or '[No Output]'}"
    except Exception as e:
        return f"Script run error: {e}"
