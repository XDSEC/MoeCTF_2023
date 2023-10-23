from time import sleep
from os import environ, system, popen
from random import randint
from sys import argv

# The cat spawns many processes so you won't find him!
for _ in range(randint(100, 1000)):
    system("true")

if argv[1] != "flag{HIDDEN}":
    # The cat spawns himself again to hide the flag!
    environ["CATSFLAG"] = argv[1]
    popen(f"python {__file__} flag{{HIDDEN}}")
else:
    # After securely hiding himself, he sleeps before escaping to his universe...
    # Note that Doggy starts hiding exactly when the environment starts.
    # So if Doggy escapes in 5 mins, you will HAVE TO RESET your environment!
    sleep(300)
    exit()
