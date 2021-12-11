<?php
$input=file("input_11_1.txt");
$result=-1;


for ($i=0;$i<count($input);$i++) {
	$input[$i]=str_split(trim($input[$i]));
}
function flash($x,$y) {
global $input;
	$input[$x][$y]=-1;
	add_points($x-1,$y);
	add_points($x+1,$y);
	add_points($x,$y+1);
	add_points($x,$y-1);
	add_points($x-1,$y-1);
	add_points($x-1,$y+1);
	add_points($x+1,$y-1);
	add_points($x+1,$y+1);
}

function add_points($x,$y) {
global $input;
	if ($x >=0 && $y >= 0 && $x < count($input) && $y < count($input[0]) ) {
		if ($input[$x][$y] > -1) $input[$x][$y]+=1;
	}
}

for ($k=0;$k<1000;$k++) {
	$flashs=0;
        for ($i=0;$i<count($input);$i++) {
        	for ($j=0;$j<count($input[$i]);$j++) {
                        $input[$i][$j]+=1;
                }
	}
	for ($i=0;$i<count($input);$i++) {
		$iold=$i;
        	for ($j=0;$j<count($input[$i]);$j++) {
		       	if ($input[$i][$j] > 9) {
				flash($i,$j);
				$flashs+=1;
				$j=count($input[$i]);
				$iold=-1;
			}
        	}
		$i=$iold;

	}
        for ($i=0;$i<count($input);$i++) {
                for ($j=0;$j<count($input[$i]);$j++) {
			if ($input[$i][$j] == -1) $input[$i][$j]=0;
		}
	}
	if ($flashs == count($input)*count($input[0]) && $result == -1) $result=$k+1;
}

echo "Result: $result";

?>
