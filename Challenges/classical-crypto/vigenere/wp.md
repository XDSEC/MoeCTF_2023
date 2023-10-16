1. the length of key <= 8
2. have you know a part of the flag?


```Cyberchef
Vigenère_Decode('goodjob')
```


写脚本爆破一下 key前面六位复原flag格式的moectf，然后发现md5不对，那就是key还有 1 or 2 位，直接爆破即可
