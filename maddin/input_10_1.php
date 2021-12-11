<?php
$input=file("input_10_1.txt");
$allowedo="-{[(<";
$allowedc="-}])>";
$result=0;
function getpoints($c) {
$p=0;
if ($c == ")") $p=3;
if ($c == "]") $p=57;
if ($c == "}") $p=1197;
if ($c == ">") $p=25137;
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
					$result+=getpoints($line[$j]);
					$line=[];
				} else {
					array_splice($opens,-1);
				}
			}
		}
	}
}
echo "Result: $result";
?>
