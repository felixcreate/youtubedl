<?php
    if(isset($_GET["url"])) {
        $contents = file_get_contents($_GET["url"]);
        $dom = new DOMDocument();
        $dom->loadHTML($contents);
        $metal = $dom->getElementsByTagName("meta");
        $s = 0;
        for($i = 0;$i<count($metal);$i++) {
            if($metal[$i]->getAttribute("property") == "og:title") {
                $s = 1;
            break;
            }
        }
        if($s == 1) {
            echo "y";
        }
        else {
            echo "n";
        }
    }
?>
