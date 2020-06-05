<?php
//Jacob Banghart
//Last editied 6/5/2020
$printable = fopen("index.php", "r") or die ("Unable to open");
while(!feof($printable)){
    echo fgets($printable) . "<" . "br>";
}
fclose($printable);