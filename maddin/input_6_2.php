<?php
$input=file("input_6_1.txt");
$data=explode(",",trim($input[0]));
$fishes=array_fill(0,9,0);
$result=0;

for ($i=0;$i<count($data);$i++) {
        $fishes[$data[$i]]+=1;
}

for ($i=0;$i<256;$i++){
        $fishes_born=$fishes[0];
        array_splice($fishes,0,1);
        $fishes[6]+=$fishes_born;
        $fishes[8]=$fishes_born;
}

for ($i=0;$i<count($fishes);$i++) {
        $result+=$fishes[$i];
}
echo "Result: $result";
?>
