<?php
    if(isset($_GET["url"])) {
        $url = $_GET["url"];
        echo file_get_contents($url);
    }
?>
