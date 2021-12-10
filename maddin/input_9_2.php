<?php
$input=file("input_9_1.txt");
$data=array_fill(0,count($input),array_fill(0,strlen(trim($input[0])),"x"));
$map=array_fill(0,count($input),array_fill(0,strlen(trim($input[0])),"x"));;
$result=[1,0];

function get_surroundings($x,$y) {
global $map;
	$counts=1;
	$map[$x][$y]=9;
	if ($y==0) {
		if ($map[$x][$y+1] < 9) $counts+=get_surroundings($x,$y+1);
		if ($x<count($map)-1) if ($map[$x+1][$y] < 9) $counts+=get_surroundings($x+1,$y);
		if ($x>0) if ($map[$x-1][$y] < 9) $counts+=get_surroundings($x-1,$y);
	}
	if ($y > 0 && $y < count($map[$x])-1) {
		if ($map[$x][$y-1] < 9) $counts+=get_surroundings($x,$y-1);
		if ($map[$x][$y+1] < 9) $counts+=get_surroundings($x,$y+1);
		if ($x<count($map)-1) if ($map[$x+1][$y] < 9) $counts+=get_surroundings($x+1,$y);
		if ($x>0) if ($map[$x-1][$y] < 9) $counts+=get_surroundings($x-1,$y);
	}
	if ($y==count($map[$x])-1) {
		if ($map[$x][$y-1] < 9) $counts+=get_surroundings($x,$y-1);
		if ($x<count($map)-1) if ($map[$x+1][$y] < 9) $counts+=get_surroundings($x+1,$y);
		if ($x>0) if ($map[$x-1][$y] < 9) $counts+=get_surroundings($x-1,$y);
	}
	return $counts;
}

for ($i=0;$i<count($input);$i++) {
	$row=str_split(trim($input[$i]));
	for ($j=0;$j<count($row);$j++) {
		$map[$i][$j]=$row[$j];
		$rowup=array_fill(0,count($row),9);
		$rowdn=array_fill(0,count($row),9);
		if ($i>0) $rowup=str_split(trim($input[$i-1]));
		if ($i<count($input)-1) $rowdn=str_split(trim($input[$i+1]));
		if ($j>0 && $j<count($row)-1) if ($row[$j-1] > $row[$j] && $rowdn[$j] > $row[$j] && $rowup[$j] > $row[$j] && $row[$j+1] > $row[$j]) $data[$i][$j]=$row[$j];
		if ($j==0) if ($row[$j+1] > $row[$j] && $rowdn[$j] > $row[$j] && $rowup[$j] > $row[$j]) $data[$i][$j]=$row[$j];
		if ($j==count($row)-1) if ($row[$j-1] > $row[$j] && $rowdn[$j] > $row[$j] && $rowup[$j] > $row[$j]) $data[$i][$j]=$row[$j];
	}
}

for ($i=0;$i<count($data);$i++) {
	for ($j=0;$j<count($data[$i]);$j++) {
		if ($data[$i][$j]!="x") {
			$res=get_surroundings($i,$j);
			$l=count($result);
			for ($k=0;$k<$l;$k++) {
				if ($result[$k] < $res) {
					array_splice($result,$k,0,$res);
					$res=-1;
				}
			}
		}
	}
}
$res=1;
for ($i=0;$i<3;$i++) {
	$res*=$result[$i];
}
echo "Result: $res";
?>
