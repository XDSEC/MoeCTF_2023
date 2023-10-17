from Crypto.Util.number import *

with open("key.txt", "r") as fs:
    key = int(fs.read().strip())
with open("flag.txt", "rb") as fs:
    flag = fs.read().strip()
assert len(flag) == 72

m = bytes_to_long(flag)

base = bytes_to_long(b"koito")
iv = 3735927943

def blockize(long):
    out = []
    while long > 0:
        out.append(long % base)
        long //= base
    return list(reversed(out))


blocks = blockize(m)


def encrypt_block_cbc(blocks, iv, key):
    encrypted = [iv]
    for i in range(len(blocks)):
        encrypted.append(blocks[i] ^ encrypted[i] ^ key)
    return encrypted[1:]


print(encrypt_block_cbc(blocks, iv, key))
# [8490961288, 122685644196, 349851982069, 319462619019, 74697733110, 43107579733, 465430019828, 178715374673, 425695308534, 164022852989, 435966065649, 222907886694, 420391941825, 173833246025, 329708930734]