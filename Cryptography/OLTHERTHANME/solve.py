from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import binascii

def des_decrypt(encrypted_message, key):
    encrypted_bytes = binascii.unhexlify(encrypted_message)
    
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    
    return decrypted_bytes.decode('utf-8')

encrypted_message = "facfdd1b94c011fcb5d36f73852f726569ecb0be70d1d3c1f83baaec88edf1b55b07d1ef3735e66fd964cf2f6f173e179688ca4e207f42d8"
key = "12345671"

decrypted_message = des_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
