from Crypto.Util.number import isPrime
from random import getrandbits

with open("flag.txt","rb") as fs:
    flag = fs.read().strip()

def diffie_hellman(p, flag):
    alice_privKey = getrandbits(1024)
    alice_pubKey = pow(7, alice_privKey, p)
    bob_privKey = getrandbits(1024)
    bob_pubKey = pow(7, bob_privKey, p)

    superkey = pow(bob_pubKey, alice_privKey, p)
    m = int.from_bytes(flag, 'big')
    return (m * superkey) % p, alice_pubKey, bob_pubKey


from typing import Callable

def chall(input:Callable[[str],None], print:Callable[[str],None]):
    p = int(input("P = "))
    if isPrime(p) and p.bit_length() >= 1024:
        c, alice_pubKey, bob_pubKey = diffie_hellman(p, flag)
        print("Alice's public key: {}".format(alice_pubKey))
        print("Bob's public key: {}".format(bob_pubKey))
        print("Ciphertext: {}".format(c))
    else:
        print("Invalid P")