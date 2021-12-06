<?php
$input=file("input_6_1.txt");
$data=explode(",",trim($input[0]));
$fishes=[0,0,0,0,0,0,0,0,0];
for ($i=0;$i<count($data);$i++) {
$fishes[$data[$i]]+=1;
}
for ($i=0;$i<256;$i++){

$fishes_born=$fishes[0];
$fishes[0]=$fishes[1];
$fishes[1]=$fishes[2];
$fishes[2]=$fishes[3];
$fishes[3]=$fishes[4];
$fishes[4]=$fishes[5];
$fishes[5]=$fishes[6];
$fishes[6]=$fishes[7]+$fishes_born;
$fishes[7]=$fishes[8];
$fishes[8]=$fishes_born;
}
echo "Result: ".($fishes[0]+$fishes[1]+$fishes[2]+$fishes[3]+$fishes[4]+$fishes[5]+$fishes[6]+$fishes[7]+$fishes[8]);
?>
