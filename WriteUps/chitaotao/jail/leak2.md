```python
fake_key_into_local_but_valid_key_into_remote = "moectfisbestctfhopeyoulikethat"
print("Hey Guys,Welcome to the moeleak challenge.Have fun!.")
print("| Options: \
|       [V]uln \
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

`vars` `locals` `globals` 都不行，jail中有用到help pager，这题事实上是help的正常用法，因为__main__也是模块

```python
>>> e
Hey Guys,Welcome to the moeleak challenge.Have fun!.
| Options: 
|       [V]uln 
|       [B]ackdoor
>>> v
you need to 
code >> help()     

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> __main__    
Help on module __main__:

NAME
    __main__

FUNCTIONS
    func_filter(s)

DATA
    CHALLENGE_SOURCE_CODE = '\n    fake_key_into_local_but_valid_key_into_...
    WELCOME = '\n  __  __  ___       _      ______        _  __ ...       ...
    __annotations__ = {}
    challenge_choice = 'v'
    choice = 'e'
    code = 'help()'
    key_f5ee1754b2e73acf = '43610e2ef5ee1754b2e73acf35348dd5'

FILE
    /home/ctf/server.py


help> 
```