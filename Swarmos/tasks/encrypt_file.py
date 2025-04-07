from utils.encryption import encrypt_file

async def handle(data):
    filepath = data.get("filepath")
    password = data.get("password")
    output_path = encrypt_file(filepath, password)
    return f"Encrypted to {output_path}"
