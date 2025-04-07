# src/tasks/encrypt_file.py
from cryptography.fernet import Fernet

def run(args):
    if len(args) < 2:
        return "Usage: encrypt_file <input> <output>"
    input_file, output_file = args
    key = Fernet.generate_key()
    cipher = Fernet(key)
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        return f"File encrypted to {output_file}.\nKey (save it!): {key.decode()}"
    except Exception as e:
        return f"Encryption error: {e}"
