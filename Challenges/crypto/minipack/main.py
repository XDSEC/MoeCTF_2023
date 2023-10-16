import random

with open("flag.txt", "rb") as fs:
    flag = fs.read().strip()

assert len(flag) == 72
m = int.from_bytes(b"\xff" + flag + b"\xff", "big")


def long2bits(long):
    bits = []
    while long > 0:
        bits.append(long & 1)
        long >>= 1
    return list(reversed(bits))


def genkey(len):
    sum = 0
    out = []
    for i in range(len):
        delta = random.randint(1, 10000)
        x = sum + delta
        out.append(x)
        sum += x
    return out


key = genkey(74 * 8)

with open("key.txt", "w") as fs:
    fs.write(str(key))


def encrypt(m, keys):
    data = long2bits(m)
    assert len(data) == len(keys)
    return sum((k if (p == 1) else 1) for p, k in zip(data, keys))


with open("ciphertext.txt", "w") as fs:
    fs.write(str(encrypt(m, key)))
