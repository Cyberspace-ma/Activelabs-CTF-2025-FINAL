from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii

def des_encrypt(message, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long")
    
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    
    padded_message = pad(message.encode('utf-8'), DES.block_size)
    
    encrypted_bytes = cipher.encrypt(padded_message)
    
    return binascii.hexlify(encrypted_bytes).decode('utf-8')

message = input("Enter the message to encrypt: ")
key = input("Enter the 8-byte key: ")

encrypted_message = des_encrypt(message, key)
print(f"Encrypted Message (Hex): {encrypted_message}")
