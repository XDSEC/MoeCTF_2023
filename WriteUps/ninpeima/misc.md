# Misc
## 1.base乐队
```
将HFUEULC5HEZG42DGHFGDWSCTHRCUIUSVHFGDWS2EGZMCCRDKG5XG2LDEHFUTYYZGHJSUMKKDGVZDELBRHBIW4UCQGZLGOP2SHEYV44ZOHEZFYXCZHEYUIV2VGEXVK4KRHBWFWY2OHVMWSYCKG5XFCZTBHEZC6I2WHJST2ZK4HEXTSMDSHA3CKZRZGRNHI4LL
粘贴到CyberChef得到bYeNQXYZXbXZQfW31FGzzD0m0FHQ9RR85FFQYMB9M=lmo2ku11z0uiz=

显然是base64但等号不在末尾，通过栅栏密码放到末尾后再解得flag：
```

```
moectf{Th4_6@nd_1nc1ud45_F3nc4_@nd_b@s3}
```

---

## 2.build_near_lake
#### 查看图片信息可看到拍摄日期，通过百度识图发现此处位于厦大，找厦大图片视频锁定为厦大某座图书馆，百度地图搜索厦大图书馆，一个个试就可以了。最终flag:
`` moectf{P0sT_Y0uR_Ph0T0_wiTh_0Riginal_File_is_n0T_a_g00d_idea_YlJf!M3rux}
``

## 3.奇怪的压缩包
#### 发现此压缩包实际为ppt打开后通过实验最后发现有部分被图片遮挡，最后一部分在备注里，最终flag:
```
moectf{2ip_?_n0_i4_pp4x!}
```

## 4.烫烫烫
#### 将文本放入CyberChef得到
```
这是你的flag：
a9736d8ad21107398b73324694cbcd11f66e3befe67016def21dcaa9ab143bc4405be596245361f98db6a0047b4be78ede40864eb988d8a4999cdcb31592fd42c7b73df3b492403c9a379a9ff5e81262

但是flag用AES加密了，key是下面这行字的sha256（hash值的开头是b34edc782d68fda34dc23329）
所以说，codepage真的很重要啊（
```
#### 最终得到flag:
```
moectf{codep@ge_pl@ys_@n_iMport@nt_role_in_intern@tion@liz@tion_g92WPIB}
```


## 5.尊嘟假嘟？
#### 将文本放入尊嘟假嘟翻译器得到
```
cipher: rY5Ah8BtsYYatLEPu8YCPU22Gr5PQt8YGDKkvb4bk3D4JJeEe5kgCpoEqgRzsM7m9d8jEtE3LUoKpULQnMcuAunU1gtpzC5kSUxFctFTNCMZVHLHZNCo5akzKMRY5bbyBP7RNUeGDEYoUc
key: the tailing 8 bytes of hash of "zundujiadu?" which begin with b6091904cdfb
iv: the end 8 bytes of hash of "dududu?" which begin with 272bf1da2207

hint1: how do Bitcoin addresses encode?
hint2: the name of cryptosystem is "bl****sh"
```
#### 得到
```
key=57E55C126F1557B3;iv=67E9FCA0871F9834
```
#### https://gchq.github.io/CyberChef/#recipe=From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)Blowfish_Decrypt(%7B'option':'Hex','string':'57E55C126F1557B3'%7D,%7B'option':'Hex','string':'67E9FCA0871F9834'%7D,'CBC','Raw','Raw')From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=clk1QWg4QnRzWVlhdExFUHU4WUNQVTIyR3I1UFF0OFlHREtrdmI0YmszRDRKSmVFZTVrZ0Nwb0VxZ1J6c003bTlkOGpFdEUzTFVvS3BVTFFuTWN1QXVuVTFndHB6QzVrU1V4RmN0RlROQ01aVkhMSFpOQ281YWt6S01SWTViYnlCUDdSTlVlR0RFWW9VYw

---

## 6.打不开的图片
#### 第一个文件头不对改完后看属性得到一段hex放入CyberChef得到flag:
```
moectf{XDU_i5_v3ry_6e@u2ifu1}
```
#### 第二个放入010发现为实际为png图片修改文件头后发现flag:
```
moectf{D0_yOu_1ik3_BO7@ck_?}
```

## 7.weird_package
#### 将压缩包用7—zip打开后发现有9个文件;经过一系列实验发现为Deflate字符串且前8个都是假的，第九个为真,搜索在线Deflate转文本得出一段base64编码，解码后得到flag
```
Deflate:FcPBCsIwDADQXzJuHnL0UEIFGbZLtuxmN4tIIoIgY18/PLwyoGmT/AFLVEk1kYUR7LcIhgLIf5mk6nh5ZbLj1GONw3q7kk0lfDzyYZvf0nY8n8T1mR3bO8O3689boRV3
解密后：bW9lY3Rme1dIYVRfRGlEX1lvdV9Eb19Ub19USGVfYXJjSGl2ZT9fIWxQMGlZbEpmIU0zcnV4OUc5VmYhSm94aU1sOTAzbGx9
base64解码：moectf{WHaT_DiD_You_Do_To_THe_arcHive?_!lP0iYlJf!M3rux9G9Vf!JoxiMl903ll}
```

## 8.狗子的照片
#### 搜索stegonline，将照片拖入便可发现flag：
```
moec  tf{D0ggy  _H1dd3n_  1n_Pho7o  _With_LS  B!}
```

## 9.你想要flag吗？
#### 将文件拖入Au发现杂音部分隐藏信息
```
key:Bulbasaur
pwd:youseeme
```
#### linux中输入
```
steghide extract -sf 1.WAV -xf 1.txt
```
#### 密码为youseeme获取音频隐藏信息
搜索在线rabbit解密解出flag：
```
Mu5ic_1s_v3ry_1nt23esting_!
```
#### 套上moectf{}即可