<?php
// 允许的最大文件大小（单位：字节）
$maxFileSize = 2 * 1024 * 1024; // 2MB

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $uploadDir = "uploads/"; // 图片上传目录
    $imageFile = $_FILES["image"];

    // 检查文件大小
    if ($imageFile["size"] > $maxFileSize) {
        echo "文件大小超过限制（最大允许 " . ($maxFileSize / (1024 * 1024)) . "MB）。";
    } else {
        // 使用 fileinfo 扩展判断文件类型
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        $imageType = finfo_file($finfo, $imageFile["tmp_name"]);
        finfo_close($finfo);

        $allowedImageTypes = ['image/jpeg', 'image/png', 'image/gif'];

        if (in_array($imageType, $allowedImageTypes)) {
            // 生成一个唯一的文件名
            $uniqueFileName = uniqid() . '_' . $imageFile["name"];
            $destinationPath = "../uploads/" . $uniqueFileName;

            // 将文件从临时位置移动到目标位置
            if (move_uploaded_file($imageFile["tmp_name"], $destinationPath)) {
                $imageUrl = "images.php?name=" . $uniqueFileName;
                echo '<a href="'.$imageUrl.'">查看</a>';
                exit;
            } else {
                echo "文件上传失败。";
            }
        } else {
            echo "只允许上传图片文件（JPEG、PNG 或 GIF）。";
        }
    }
}
?>
