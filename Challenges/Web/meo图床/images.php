<?php
if (isset($_GET['name'])) {
    $name = $_GET['name'];
    // 显示图片并设置正确的 MIME 类型
    $imageData = file_get_contents('../uploads/'.$name);
    header("Content-Type: " . 'image/png');
    echo $imageData;
}
?>
