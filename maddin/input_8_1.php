<?php
$input=file("input_8_1.txt");
$result=0;

for ($i=0;$i<count($input);$i++) {
	$data=explode(" | ",trim($input[$i]));
	$segments=explode(" ",$data[1]);
	for ($j=0;$j<count($segments);$j++) {
		if (strlen($segments[$j])==2 || strlen($segments[$j])==3 || strlen($segments[$j])==4 || strlen($segments[$j])==7) $result+=1;
	}
}

echo "Result: ".$result;
?>
