import random

with open("flag.txt", "r") as f:
    flag = f.read().strip()


class LCG:
    def set_params(self):
        self.m = random.randint(10000, 20000)
        self.a = random.randint(10000, 20000)
        self.c = random.randint(1, self.a-1)
        self.x = random.randint(0, self.m-1)

    def get_all_output(self):
        x0 = self.x
        s = set()
        while (t := self()) not in s:
            s.add(t)
        self.x = x0
        return s

    def __init__(self):
        self.set_params()
        while len(self.get_all_output()) < 10:
            self.set_params()

    def __call__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

from typing import Callable

def chall(input:Callable[[str],None], print:Callable[[str],None]):
    from hashlib import md5
    from string import ascii_letters
    s = "".join(random.choices(ascii_letters, k=8))
    h = md5(s.encode()).hexdigest()
    print(f"<!> md5(XXXX+{s[4:]}) == {h}")
    i = input("Give me XXXX: ")
    if md5((i + s[4:]).encode()).hexdigest() != h:
        print("<!> ACCESS DENIED <!>")
        return
    inst = LCG()
    print("Let's play a simple game! If you can guess the right number, I will give your the flag! You have 10 tries")
    for tries in range(10):
        i = input(f"Give me a number, you have failed for {tries} times: ")
        if int(i) == (right := inst()):
            print(f"Congurations! You win the game! Your flag is here: {flag}")
            break
        else:
            print(f"Oh, you are wrong! The right number is {right}")
