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
