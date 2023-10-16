flag = open('flag.txt','rb').read()
assert flag.startswith(b'moectf{') and flag.endswith(b'}')
article = open('article.txt','rb').read()

import random

strxor = lambda x,y: bytes([a^b for a,b in zip(x,y)])

result = []

for i in range(100):
    range_start = random.randint(0, len(article) - len(flag))
    mask = article[range_start:range_start + len(flag)]
    result.append(strxor(flag,mask))

with open("result.log","w") as fs:
    fs.writelines([str(i)+"\n" for i in result])
