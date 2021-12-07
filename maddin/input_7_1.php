<?php
$input=file("input_7_1.txt");
$data=explode(",",trim($input[0]));
$crabs=array_fill(0,2000,0);
$result=0;
$fuel=array_fill(0,2000,0);

for ($i=0;$i<count($data);$i++) {
	$crabs[$data[$i]]+=1;
}

for ($i=0;$i<count($crabs);$i++) {
	for ($j=0;$j<count($crabs);$j++) {
		$fuel[$i]+=($crabs[$j]*abs($i-$j));
	}
}

$result=$fuel[0];

for ($i=0;$i<count($fuel);$i++) {
	if ($fuel[$i]<$result) {
		$result=$fuel[$i];
	}
}
echo "Result: ".$result;
?>
