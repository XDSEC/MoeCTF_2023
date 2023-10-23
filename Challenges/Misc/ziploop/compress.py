from subprocess import run
from random import randint
from time import sleep

last_filename = "flag.txt"
for i in range(10000):
    match randint(0, 2):
        case 0:
            run(f"zip shell{i}.zip {last_filename}", shell=True)
            run(f"rm {last_filename}", shell=True)
            last_filename = f"shell{i}.zip"
        case 1:
            run(f"7z a shell{i}.7z {last_filename}", shell=True)
            run(f"rm {last_filename}", shell=True)
            last_filename = f"shell{i}.7z"
        case 2:
            run(f"tar -czf shell{i}.tar.gz {last_filename}", shell=True)
            run(f"rm {last_filename}", shell=True)
            last_filename = f"shell{i}.tar.gz"


print(f"final file: {last_filename}")
