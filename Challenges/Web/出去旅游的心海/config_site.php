<?php

// 获取访问者的url
$visitor_uri = $_SERVER['HTTP_HOST'];

// 要更新的url
$new_site_url = $visitor_uri . '/wordpress';

// 连接到数据库服务器
$servername = "127.0.0.1";
$username = "wp_user";
$password = "d6nyPBdjNYmF31EV";
$dbname = "wordpress";

// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("数据库连接失败: " . $conn->connect_error);
}

// 更新站点地址和WordPress地址
$sql = "UPDATE wp_options SET option_value='$new_site_url' WHERE option_name='siteurl' OR option_name='home'";

if ($conn->query($sql) === TRUE) {

    // 读取原始的 wp-config.php 内容
    $wp_config_file = '/var/www/html/wordpress/wp-config.php';
    $config_content = file_get_contents($wp_config_file);

    // 构造要插入的新内容
    $new_config_content = "define( 'WP_HOME', '$new_site_url' );\n";
    $new_config_content .= "define( 'WP_SITEURL', '$new_site_url' );\n";

    // 将新内容插入到 /* That's all, stop editing! Happy publishing. */ 之前
    $stop_editing_line = "/* That's all, stop editing! Happy publishing. */";
    $new_config_content = str_replace($stop_editing_line, $new_config_content . $stop_editing_line, $config_content);
    echo $new_config_content;

    // 将更新后的内容写回到 wp-config.php 文件
    if (file_put_contents($wp_config_file, $new_config_content) !== false) {
        // 输出成功消息
        echo "WordPress站点的url已自动调整为：$new_site_url";
    } else {
        echo "更新失败，请检查是否有写入权限。";
    }
} else {
    echo "更新失败: " . $conn->error;
}
?>
