from Crypto.Util.number import *
from os import urandom

round = 2
flag = open("./secret", "rb").read().strip()


def f(m, key):
    m = m ^ (m >> 4)
    m = m ^ (m << 5)
    m = m ^ (m >> 8)
    m ^= key
    m = (m * 1145 + 14) % 2**64
    m = (m * 1919 + 810) % 2**64
    m = (m * key) % 2**64
    return m


def enc(m, key, round):
    key = bytes_to_long(key)
    left = bytes_to_long(m[:8])
    right = bytes_to_long(m[8:])
    for i in range(round):
        left, right = right, f(right, key) ^ left
    left, right = right, left
    return long_to_bytes(left).rjust(8, b"\x00") + long_to_bytes(right).rjust(8, b"\x00")


def padding(m):
    mlen = len(m)
    pad = 16 - mlen % 16
    return m + pad * bytes([pad])


def ecb_enc(m, key):
    m = padding(m)
    mlen = len(m)
    c = b""
    for i in range(mlen // 16):
        c += enc(m[i * 16 : i * 16 + 16], key, round)
    return c


key = urandom(8)

print(ecb_enc(padding(flag), key))
# b'B\xf5\xd8gy\x0f\xaf\xc7\xdf\xabn9\xbb\xd0\xe3\x1e0\x9eR\xa9\x1c\xb7\xad\xe5H\x8cC\x07\xd5w9Ms\x03\x06\xec\xb4\x8d\x80\xcb}\xa9\x8a\xcc\xd1W\x82[\xd3\xdc\xb4\x83P\xda5\xac\x9e\xb0)\x98R\x1c\xb3h'
