import base64
import ctypes
import itertools
import math
from ctypes import *


class tea:
    delta = 0x9e3779b9
    @classmethod
    def encrypt(cls, v, k):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = cls.delta
        k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

        total = c_uint32(0)
        for i in range(32):
            total.value += delta
            v0.value += ((v1.value << 4) + k0) ^ (v1.value +
                                                  total.value) ^ ((v1.value >> 5) + k1)
            v1.value += ((v0.value << 4) + k2) ^ (v0.value +
                                                  total.value) ^ ((v0.value >> 5) + k3)

        return v0.value, v1.value

    @classmethod
    def decrypt(cls, v, k):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = cls.delta
        k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

        total = c_uint32(delta * 32)
        for i in range(32):
            v1.value -= ((v0.value << 4) + k2) ^ (v0.value +
                                                  total.value) ^ ((v0.value >> 5) + k3)
            v0.value -= ((v1.value << 4) + k0) ^ (v1.value +
                                                  total.value) ^ ((v1.value >> 5) + k1)
            total.value -= delta

        return v0.value, v1.value


class xtea:
    delta = 0x9E3779B9
    @classmethod
    def encrypt(cls, v, key):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = cls.delta

        total = c_uint32(0)
        for i in range(32):
            v0.value += (((v1.value << 4) ^ (v1.value >> 5)) +
                         v1.value) ^ (total.value + key[total.value & 3])
            total.value += delta
            v1.value += (((v0.value << 4) ^ (v0.value >> 5)) +
                         v0.value) ^ (total.value + key[(total.value >> 11) & 3])

        return v0.value, v1.value

    @classmethod
    def decrypt(cls, v, key):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = cls.delta

        total = c_uint32(delta * 32)
        for i in range(32):
            v1.value -= (((v0.value << 4) ^ (v0.value >> 5)) +
                         v0.value) ^ (total.value + key[(total.value >> 11) & 3])
            total.value -= delta
            v0.value -= (((v1.value << 4) ^ (v1.value >> 5)) +
                         v1.value) ^ (total.value + key[total.value & 3])

        return v0.value, v1.value



class xxtea:
    delta = 0x9e3779b9
    @staticmethod
    def MX(z, y, total, key, p, e):
        temp1 = (z.value>>5 ^ y.value<<2) + (y.value>>3 ^ z.value<<4)
        temp2 = (total.value ^ y.value) + (key[(p&3) ^ e.value] ^ z.value)
        
        return c_uint32(temp1 ^ temp2)


    @classmethod
    def encrypt(cls, n, v, key):
        v = list(v)
        delta = cls.delta
        rounds = 6 + 52//n

        total = c_uint32(0)
        z = c_uint32(v[n-1])
        e = c_uint32(0)
        
        while rounds > 0:
            total.value += delta  
            e.value = (total.value >> 2) & 3
            for p in range(n-1):
                y = c_uint32(v[p+1])
                v[p] = c_uint32(v[p] + cls.MX(z,y,total,key,p,e).value).value
                z.value = v[p]
            y = c_uint32(v[0])
            v[n-1] = c_uint32(v[n-1] + cls.MX(z,y,total,key,n-1,e).value).value
            z.value = v[n-1]
            rounds -= 1 

        return v


    @classmethod
    def decrypt(cls, n, v, key):
        v = list(v)
        delta = cls.delta
        rounds = 6 + 52//n 
        
        total = c_uint32(rounds * delta)
        y = c_uint32(v[0])
        e = c_uint32(0)

        while rounds > 0:
            e.value = (total.value >> 2) & 3
            for p in range(n-1, 0, -1):
                z = c_uint32(v[p-1])
                v[p] = c_uint32((v[p] - cls.MX(z,y,total,key,p,e).value)).value
                y.value = v[p]
            z = c_uint32(v[n-1])  
            v[0] = c_uint32(v[0] - cls.MX(z,y,total,key,0,e).value).value
            y.value = v[0]  
            total.value -= delta
            rounds -= 1

        return v 


def __sanitize_key(key):
    if isinstance(key, str):
        key = key.encode()
    if isinstance(key, bytes) or isinstance(key, bytearray):
        key = key.ljust(16, b'\x00')
        key = str2vec(key[:16])
    return key


def __sanitize_plaintext(plaintext):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    if isinstance(plaintext, bytes) or isinstance(plaintext, bytearray):
        plaintext = str2vec(plaintext)
    return plaintext


def __sanitize_ciphertext(ciphertext):
    if isinstance(ciphertext, str):
        ciphertext = base64.b64decode(ciphertext.encode())
    if isinstance(ciphertext, bytes) or isinstance(ciphertext, bytearray):
        ciphertext = str2vec(ciphertext)
    return ciphertext


def encrypt(plaintext, key, cls, no_str=True, n=None):
    """
    Encrypts a message using a 16-character key.
    :param plaintext:
        The message to encode.  *Must* be a utf8 string but can have any length.
    :param key:
        The encryption key used to encode the plaintext message.  *Must* be a utf8 string and 16 characters long.
    :return:
        A base64 utf8 string of the encrypted message.
    """
    if not plaintext:
        return ''

    key = __sanitize_key(key)

    plaintext = __sanitize_plaintext(plaintext)

    if cls == xxtea:
        res = [num for chunk in chunks(plaintext, n) for num in cls.encrypt(n, chunk, key)]
    else:
        res = [num for chunk in chunks(plaintext, 2) for num in cls.encrypt(chunk, key)]
    if no_str:
        return res

    return base64.b64encode(vec2str(res)).decode()


def decrypt(ciphertext, key, cls, no_str=False, n=None):
    """
    Decrypts a message using a 16-character key.
    :param ciphertext:
        The encrypted message to decode as a base64 utf8 string.
    :param key:
        The encryption key used to encode the plaintext message.  *Must* be a utf8 string and 16 characters long.
    :return:
        A utf8 string of the decrypted message.
    """
    if not ciphertext:
        return ''

    key = __sanitize_key(key)

    ciphertext = __sanitize_ciphertext(ciphertext)

    # print(f"key: {key}, ciphertext: {ciphertext}")
    
    if cls == xxtea:
        res = [num for chunk in chunks(ciphertext, n) for num in cls.decrypt(n, chunk, key)]
    else:
        res = [num for chunk in chunks(ciphertext, 2) for num in cls.decrypt(chunk, key)]
    if no_str:
        return res

    return vec2str(res).decode()


# def _encipher(v, k):
#     """
#     TEA encipher algorithm.  Encodes a length-2 vector using a length-4 vector as a length-2 vector.  

#     Compliment of _decipher.
#     :param v:
#         A vector representing the information to be enciphered.  *Must* have a length of 2.
#     :param k:
#         A vector representing the encryption key.  *Must* have a length of 4.
#     :return:
#         A length-2 vector representing the encrypted information v.
#     """
#     y, z = [ctypes.c_uint32(x)
#             for x in v]
#     sum = ctypes.c_uint32(0)
#     delta = 0x9E3779B9

#     for n in range(32, 0, -1):
#         sum.value += delta
#         y.value += (z.value << 4) + k[0] ^ z.value + \
#             sum.value ^ (z.value >> 5) + k[1]
#         z.value += (y.value << 4) + k[2] ^ y.value + \
#             sum.value ^ (y.value >> 5) + k[3]

#     return [y.value, z.value]


# def _decipher(v, k):
#     """
#     TEA decipher algorithm.  Decodes a length-2 vector using a length-4 vector as a length-2 vector.

#     Compliment of _encipher.
#     :param v:
#         A vector representing the information to be deciphered.  *Must* have a length of 2.
#     :param k:
#         A vector representing the encryption key.  *Must* have a length of 4.
#     :return:
#         The original message.
#     """
#     y, z = [ctypes.c_uint32(x)
#             for x in v]
#     sum = ctypes.c_uint32(0xC6EF3720)
#     delta = 0x9E3779B9

#     for n in range(32, 0, -1):
#         z.value -= (y.value << 4) + k[2] ^ y.value + \
#             sum.value ^ (y.value >> 5) + k[3]
#         y.value -= (z.value << 4) + k[0] ^ z.value + \
#             sum.value ^ (z.value >> 5) + k[1]
#         sum.value -= delta

#     return [y.value, z.value]


def chunks(iterable, n):
    """
    Iterates through an iterable in chunks of size n.
    :param iterable:
        Any iterable.  Must have a length which is a multiple of n, or the last element will not contain n elements.
    :param n:
        The size of the chunks.
    :return:
        A generator that yields elements in chunks of size n.
    """
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def str2vec(value, l=4):
    """
    Encodes a binary string as a vector.  The string is split into chunks of length l and each chunk is encoded as 2 
    elements in the return value.

    Compliment of _str2vec.
    :param value:
        A binary string to encode.
    :param l:
        An optional length value of chunks.
    :return:
        A vector containing ceil(n / l) elements where n is the length of the value parameter.
    """
    if isinstance(value, str):
        value = value.encode()
    n = len(value)

    # Split the string into chunks
    num_chunks = math.ceil(n / l)
    chunks = [value[l * i:l * (i + 1)]
              for i in range(num_chunks)]

    return [sum([character << 8 * j
                 for j, character in enumerate(chunk)])
            for chunk in chunks]


def vec2str(vector, l=4):
    """
    Decodes a vector to a binary string.  The string is composed by chunks of size l for every two elements in the 
    vector.

    Compliment of _str2vec.

    :param vector:
        An even-length vector.
    :param l:
        The length of the chunks to compose the returned string.  This should match the value for l used by _str2vec.
        If the value used is smaller, than characters will be lost.
    :return:
    """
    return bytes((element >> 8 * i) & 0xff
                 for element in vector
                 for i in range(l)).replace(b'\x00', b'')
