<?php
$input=file("input_13_1.txt");
$count=0;
$result=0;




function fill($data,$fold,$axis) {
	$ret=array_fill(0,10000,array_fill(0,10000,"."));

	for ($i=0;$i<count($data);$i++) {
		if ($axis == "y") $ret[$fold-abs($data[$i][0]-$fold)][$data[$i][1]]="#";
		if ($axis == "x") $ret[$data[$i][0]][$fold-abs($data[$i][1]-$fold)]="#";
	}

return $ret;
}


$i=0;
$data=[];

while(strpos($input[$i],",") >= 1) {
	$t=explode(",",trim($input[$i]));
	$data[count($data)][0]=$t[1];
	$data[count($data)-1][1]=$t[0];
	$i++;
}

$folded=false;
for ($j=$i;$j<count($input);$j++) {
	$b=explode("=",trim($input[$j]));
	if ($b[0] == "fold along x" && $folded == false) {
		$result=fill($data,$b[1],"x");
		$folded=true;
	}
	if ($b[0] == "fold along y" && $folded == false) {
		$result=fill($data,$b[1],"y");
		$folded=true;
	}
}

for ($i=0;$i<count($result);$i++) {
	for ($j=0;$j<count($result[$i]);$j++) {
		if ($result[$i][$j] == "#") $count+=1;
	}
}

echo "Result: $count";

?>
