# WriteUp
### Author:TheValuePoint

## 打不开的图片1
用010Editor打开这个文件（加个后缀".txt"也行）

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/1a748c5a-4a13-4070-b8aa-fb82c2e76e85)

即：
6d6f656374667b5844555f69355f763372795f3665407532696675317d
然后用 https://cyberchef.org 解下密：

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/023ebc34-d4fc-4ff5-bda0-dfca362a97bb)

flag=moectf{XDU_i5_v3ry_6e@u2ifu1}

## 打不开的图片2
仍然用010Editor打开这个文件
我们对照一下这个表
然后看看文件头和文件尾：

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/399ab979-6521-4337-953c-6d4f3d5a6a9e)

尝试分别改改文件头和文件尾，发现这玩意是.png文件（一开始我还被那个后缀名骗了，天真的以为这玩意绝对是jpg……）

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/120d220e-cb88-4b99-9775-bc8f4a100840)

flag显而易见就出来了

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/9700e181-03e2-4f5a-8464-e9329c8561f5)

## building_near_lake
//一开始做这道题的时候没注意到是“发布会时间”，还以为是拍摄时间，还跑去问出题人……审题真的很重要啊。

//据说红米配天玑，越用越懵逼，不知道是不是真的（笑）

我们把这张图片用百度搜一下，轻而易举的发现这个在厦门大学翔安校区，然后用Google Earth等地图软件就可以知道这个的"WGS84"坐标，上网随便找个转换器就可以知道这个的BD09坐标了

118.317702, 24.612586

接着打开010Editor：

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/96995629-586c-409f-bede-1b1af36af07a)

这是Redmi K60E的信息：

![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/b97e70a5-b523-4198-a0cb-b5bd346e1724)

上传一下，就可以得到Flag了

## 机位查询

第一张图，可以看到这是在南宁站附近
![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/7282b0ec-7855-49ac-ac31-5c7940d1f097)

旁边是
![image](https://github.com/TheValuePoint/MoeCTF_2023/assets/58455675/d3de7b96-e717-4217-b944-43627c7a844d)

从这两建筑物就可以推断是在：
