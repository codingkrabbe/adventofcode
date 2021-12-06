<?php
$input=file("input_6_1.txt");
$data=explode(",",trim($input[0]));

for ($i=0;$i<80;$i++){
$x=count($data);
for ($j=0;$j<$x;$j++) {

if ($data[$j]==0) {
$data[$j]=6;
$data[count($data)]=8;
} else  $data[$j]-=1;
}
}
echo "Result: ".count($data);
?>
