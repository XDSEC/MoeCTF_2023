```python
__import__("os").system("sh")
```

顺便把`server.py`拿了，这对我们后面很重要（
```python
WELCOME = '''
  __  __  ___        _____        _        _                _                         _                _  ___  
 |  \/  |/ _ \      / ____| ____ | |      | |              (_)                       | |              | |/ _ \ 
 | \  / | | | | ___| |     / __ \| | ___  | |__   ___  __ _ _ _ __  _ __   ___ _ __  | | _____   _____| | | | |
 | |\/| | | | |/ _ \ |    / / _` | |/ __| | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__| | |/ _ \ \ / / _ \ | | | |
 | |  | | |_| |  __/ |___| | (_| | | (__  | |_) |  __/ (_| | | | | | | | |  __/ |    | |  __/\ V /  __/ | |_| |
 |_|  |_|\___/ \___|\_____\ \__,_|_|\___| |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|    |_|\___| \_/ \___|_|\___/ 
                           \____/                      __/ |                                                   
                                                      |___/                                                                                       
'''

CHALLENGE_SOURCE_CODE = '''
print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
print("Enter your expression and I will evaluate it for you.")
user_input_data = input("> ")
print('calc Answer: {}'.format(eval(user_input_data)))
'''

CHALLENGE_DESCRIPT = '''

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                                                                                                                                                    |
| Hey Guys,I think maybe this is your first encounter with the Jail challenge.                                                                       |
| Here is a brief description of the Jail challenge                                                                                                  |
| >   Your commands and code will run in a restricted environment you need to find a way to bypass the restricted environment to get the flags       |
|                                                                                                                                                    |
| Well, as you can see this challenge is a pyjail challenge and uses a menu where you can select functions based on relevant options.                |
| For example, type g to get the source code of the challenge, e to enter the challenge, c to get the description of the challenge, q to exit        | 
| The following description is unique to the Challenge Description function of the terminal                                                          |
|                                                                                                                                                    |
| I'm glad you understood the purpose of the menu and managed to get here, and I'm sure you've read the source code, but if you're not familiar      |    
| with python, I'd recommend checking out https://docs.python.org/3/ and https://www.runoob.com/python3/python3-tutorial.html first.                 |
| The function of the code is probably that you can type in some arithmetic expression, like 1+1 and he'll give you 2 back.But your goal is to get   |
| flag use it.                                                                                                                                       |
|                                                                                                                                                    |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

'''

CHALLENGE_HINT_FOR_BEGINNER = '''

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                                                                                                                                                    |
| Hint for beginner:                                                                                                                                 |
| 1. seems eval function isn't safe                                                                                                                  |
| 2. maybe it's really useful for u https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes                   |
|    this hint also for next 10 challenge                                                                                                            |
|                                                                                                                                                    |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

'''

print(WELCOME)
print("| Options: \n|\t[G]et Challenge Source Code \n|\t[E]nter into Challenge \n|\t[C]hallenge Description \n|\t[Q]uit \n\t")
while(1):
  choice = input(">>> ").lower().strip()
  if choice == 'g':
      print(CHALLENGE_SOURCE_CODE)
  elif choice == 'e':
    print("Welcome to the MoeCTF2023 Jail challenge.It's time to work on this calc challenge.")
    print("Enter your expression and I will evaluate it for you.")
    user_input_data = input("> ")
    print('Answer result: {}'.format(eval(user_input_data)))
  elif choice == "c":
    print(CHALLENGE_DESCRIPT)
    user_input_hint_choice = input("If you still don't know how to solve it,do you need some hint? (y/n) > ").lower().strip()
    if user_input_hint_choice == 'y':
      print(CHALLENGE_HINT_FOR_BEGINNER)
    if user_input_hint_choice == 'n':
      print("Good luck!")
  elif choice == 'q':
    print("bye~~~")
    quit()
  else:
    print("You should select valid choice!")

```