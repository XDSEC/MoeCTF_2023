import base64
from string import *
str1 = "yD9oB3Inv3YAB19YynIuJnUaAGB0um0="

string1 = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba0123456789+/"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

flag =input("welcome to moectf\ninput your flag and I wiil check it:")
enc_flag=(base64.b64encode(flag.encode())).decode()
enc_flag=enc_flag.translate(str.maketrans(string2,string1))
if enc_flag==str1:
    print("good job!!!!")
else:
    print("something wrong???")
    exit(0)
#moectf{pYc_And_Base64~}

