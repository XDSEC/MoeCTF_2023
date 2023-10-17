from Crypto.Util.number import *

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


print(ecb_enc(flag, b"wulidego"))

# b'\x0b\xa7\xc6J\xf6\x80T\xc6\xfbq\xaa\xd8\xcc\x95\xad[\x1e\'W5\xce\x92Y\xd3\xa0\x1fL\xe8\xe1"^\xad'
