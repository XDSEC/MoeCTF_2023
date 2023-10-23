from os import system
from pathlib import Path

pwd = Path.cwd()

while True:
    try:
        file = next(pwd.glob("shell*"))
    except StopIteration:
        break
    if file.name.endswith(".tar.gz"):
        system(f"tar -xvf {file.name}")
    elif file.name.endswith(".zip"):
        system(f"unzip {file.name}")
    elif file.name.endswith(".7z"):
        system(f"7z x {file.name}")
    system(f"rm {file.name}")
    