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