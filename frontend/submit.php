<?php
    if(isset($_GET["url"])) {
        $url = $_GET["url"];
        header('Connection: keep-alive');
        $name = exec("/var/www/youtube-backend/download.py ".$url);
        if($name == "error") {
            header('Isthererr: true');
        }
        else {
            if(filesize("/var/www/youtube-backend/file/".$name) != 0) {
                header('Isthererr: false');
                readfile("/var/www/youtube-backend/file/".$name);
            }
            else {
                header('Isthererr: true');
            }
        }
    }
?>
