# Classical-Crypto

## 皇帝的新密码

简单的凯撒密码，直接cyberchef解密即可

```Cyberchef
Vigenère_Decode('h')
```

## 不是皇帝的新密码

凯撒密码变种，维吉尼亚密码

```Cyberchef
Vigenère_Decode('goodjob')
```

可以写脚本爆破一下 key前面六位复原flag格式的moectf，然后发现md5不对，那就是key还有 1 or 2 位，直接爆破即可

## ezrot

ROT47，算是很常见的古典密码了

```Cyberchef
ROT47(47)
```

## 可可的新围墙

栅栏密码，但是要注意栅栏密码本身有两种，这里用的是Rail fence cipher，直接cyberchef

```Cyberchef
Rail_Fence_Cipher_Decode(3,0)
```

## 喵言喵语

Morse Code，但是做了些替换

```CyberChef
Find_/_Replace({'option':'Regex','string':'喵喵？'},'-',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'喵喵喵'},'.',true,false,true,false)
From_Morse_Code('Space','Line feed')
```