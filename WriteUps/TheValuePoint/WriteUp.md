# WriteUp(Misc)
### Author:TheValuePoint

## 打不开的图片1
用010Editor打开这个文件（加个后缀".txt"也行）
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/31edf67c-7c48-43db-a26d-114f31d9b62f)

即：
6d6f656374667b5844555f69355f763372795f3665407532696675317d
然后用 https://cyberchef.org 解下密：
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/63d314e5-14bd-481a-8006-78aaa73fd70b)

flag=moectf{XDU_i5_v3ry_6e@u2ifu1}

## 打不开的图片2
仍然用010Editor打开这个文件
我们对照一下这个表
然后看看文件头和文件尾：
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/fad6d8b4-805a-4989-99ef-8a9251db9624)

尝试分别改改文件头和文件尾，发现这玩意是.png文件（一开始我还被那个后缀名骗了，天真的以为这玩意绝对是jpg……）
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/88ecd34b-1b85-4d4c-9bdd-250b753a0abc)

flag显而易见就出来了
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/46eb701f-f7bb-45d8-ab92-818333b5441c)

## building_near_lake
###### 一开始做这道题的时候没注意到是“发布会时间”，还以为是拍摄时间，还跑去问出题人……审题真的很重要啊。
###### 据说红米配天玑，越用越懵逼，不知道是不是真的（笑）
我们把这张图片用百度搜一下，轻而易举的发现这个在厦门大学翔安校区，然后用Google Earth等地图软件就可以知道这个的"WGS84"坐标，上网随便找个转换器就可以知道这个的BD09坐标了
118.317702, 24.612586
接着打开010Editor：
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/7e407f60-450f-4d4b-a2dc-1105f155ec37)

这是Redmi K60E的信息：
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/78dc89d6-d654-4a39-8cd0-4d7c4b463943)

上传一下，就可以得到Flag了
机位查询
第一张图，可以看到这是在南宁站附近
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/defdd114-6a6e-4ac1-8045-eb333ee5c5ca)

旁边是
![image](https://github.com/XDSEC/MoeCTF_2023/assets/58455675/8ac1ff2c-7aab-4e98-8359-853543a18115)

从这两建筑物就可以推断是在：

