<?php
$input=file("input_1_1.txt");
$last=0;

for ($i=3; $i<count($input); $i++) {
        if (intval($input[$i]+$input[$i-1]+$input[$i-2])>intval($input[$i-1]+$input[$i-2]+$input[$i-3])) $last+=1;
}

echo $last;
?>
