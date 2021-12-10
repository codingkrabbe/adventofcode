<?php
$input=file("input_10_1.txt");
$allowedo="-{[(<";
$allowedc="-}])>";
$scores=[];


function getpoints($c) {
	$p=0;
	if ($c == "(") $p=1;
	if ($c == "[") $p=2;
	if ($c == "{") $p=3;
	if ($c == "<") $p=4;
	return $p;
}

for ($i=0;$i<count($input);$i++) {
	$opens=[];
	$line=str_split(trim($input[$i]));
	for ($j=0;$j<count($line);$j++) {
		if (strpos($allowedo,$line[$j])) {
			$opens[count($opens)]=$line[$j];
		} else {
			if (strpos($allowedc,$line[$j])) {
				if (ord($line[$j])-ord($opens[count($opens)-1]) > 2 || ord($line[$j])-ord($opens[count($opens)-1]) < 1) {
					$line=[];
				} else {
					array_splice($opens,-1);
				}
			}
		}
	}
	$result=0;
	if (count($line)) {
		for ($j=count($opens)-1;$j>=0;$j--) {
			$result*=5;
			$result+=getpoints($opens[$j]);
			array_splice($opens,-1);
		}
		$l=count($scores);
		if ($l == 0) {
			$scores[0]=$result;
		} else {
                        for ($k=0;$k<$l;$k++) {
                                if ($scores[$k] < $result) {
                                        array_splice($scores,$k,0,$result);
                                        $result=-1;
                                }
			}
			if ($result != -1) array_splice($scores,$l,0,$result);
		}
	}
}

echo "Result: ".$scores[(count($scores)-1)/2];
?>
