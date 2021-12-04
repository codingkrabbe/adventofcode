<?php
$input=file("input_1_1.txt");
$last=0;

for ($i=0; $i<count($input); $i++) {
        if ($input[$i]>=$input[$i-1]) $last+=1;
}

echo $last;
?>
