from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def decrypt_data(encrypted_data, key):
    try:
        key = key.encode("utf-8").ljust(32)[:32]
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted
    except Exception as e:
        return f"Decryption error: {str(e)}".encode()
