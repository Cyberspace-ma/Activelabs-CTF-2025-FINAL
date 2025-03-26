# Encrypted password from the C code
# BROzC/^M/6^E/QF26^34B00|
encrypted_output = b"\xE8\xF8\xE5\xD0\xE9\x85\xF4\xE7\x85\x9C\xF4\xEF\x85\xFB\xEC\x98\x9C\xF4\x99\x9E\xE8\x9A\x9A\xD6"

# Decryption key
ENCRYPT_KEY = 0xAA

# Decrypt the password
decrypt_output = ''.join(chr(byte ^ ENCRYPT_KEY) for byte in encrypted_output)

# Adjust the password (each character + 1)
input_password = ''.join(chr(ord(char) + 1) for char in decrypt_output)

print("Decrypted password:", decrypt_output)
print("Input password:", input_password)
