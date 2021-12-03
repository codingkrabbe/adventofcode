<?php
$input=file("input_3_1.txt");
$output1=[0,0,0,0,0,0,0,0,0,0,0,0];
$output0=[0,0,0,0,0,0,0,0,0,0,0,0];

for ($i=0; $i<count($input); $i++) {

        $itemp=str_split($input[$i]);
        for ($j=0; $j<count($itemp);$j++) {
                if ($itemp[$j]=="0") $output0[$j]+=1;
                if ($itemp[$j]=="1") $output1[$j]+=1;
        }
}

for ($i=0; $i<count($output0); $i++) {

if ($output0[$i]>$output1[$i]) {

$outputg[$i]="0";
$outpute[$i]="1";

} else {

$outputg[$i]="1";
$outpute[$i]="0";
}

}

echo (bindec(implode($outpute))*bindec(implode($outputg)));

?>
