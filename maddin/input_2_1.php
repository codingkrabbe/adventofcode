<?php
$input=file("input_2_1.txt");
$pos=0;
$depth=0;

for ($i=0; $i<count($input); $i++) {

        $itemp=explode(" ",$input[$i]);
        if ($itemp[0]=="forward") $pos+=$itemp[1];
        if ($itemp[0]=="down") $depth+=$itemp[1];
        if ($itemp[0]=="up") $depth-=$itemp[1];

}

echo $pos*$depth;
?>
