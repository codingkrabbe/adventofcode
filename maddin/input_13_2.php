<?php
$input=file("input_13_1.txt");
$count=0;
$result=0;
function fill($data) {
	$ret=array_fill(0,10,array_fill(0,50,"."));

	for ($i=0;$i<count($data);$i++) {
		$ret[$data[$i][0]][$data[$i][1]]="#";
	}

return $ret;
}


function filld($data,$fold,$axis) {
$ret=[];

	for ($i=0;$i<count($data);$i++) {
		if ($axis == "y") {
			$ret[count($ret)][0]=$fold-abs($data[$i][0]-$fold);
			$ret[count($ret)-1][1]=$data[$i][1];
		}
		if ($axis == "x") {
			$ret[count($ret)][0]=$data[$i][0];
			$ret[count($ret)-1][1]=$fold-abs($data[$i][1]-$fold);
		}
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
		$data=filld($data,$b[1],"x");
		//	$folded=true;
	}
	if ($b[0] == "fold along y" && $folded == false) {
		$data=filld($data,$b[1],"y");
		//	$folded=true;
	}
}

$result=fill($data);

for ($i=0;$i<count($result);$i++) {
	echo implode($result[$i])."\r\n";
}
?>
