<?php
$input=file("input_4_1.txt");
$i=2;
$j=0;
$found=-1;
$board=[];
$draws=explode(",",$input[0]);
$sums=[];
$result=0;

while($i < count($input)){
	$board[$j][0]=explode(" ",trim(str_replace("  "," ",$input[$i])));
	$board[$j][1]=explode(" ",trim(str_replace("  "," ",$input[$i+1])));
	$board[$j][2]=explode(" ",trim(str_replace("  "," ",$input[$i+2])));
	$board[$j][3]=explode(" ",trim(str_replace("  "," ",$input[$i+3])));
	$board[$j][4]=explode(" ",trim(str_replace("  "," ",$input[$i+4])));
	$i+=6;
	$j++;
}

for ($k=0; $k < count($draws); $k++) {
	if ($found==-1) {
		for ($l=0; $l < count($board); $l++) {
			$tsum=0;
			for ($m=0; $m < count($board[$l]); $m++) {
				for ($n=0; $n < count($board[$l][$m]); $n++) {
					if ($board[$l][$m][$n]==$draws[$k]) {
						$board[$l][$m][$n]="x";
					} else {
						if ($board[$l][$m][$n]!="x") $tsum+=$board[$l][$m][$n];
					}
				}
			}
			$sums[$l]=$tsum;
		}


		for ($l=0; $l < count($board); $l++) {
			if (implode($board[$l][0])=="xxxxx") $found=$l;
			if (implode($board[$l][1])=="xxxxx") $found=$l;
			if (implode($board[$l][2])=="xxxxx") $found=$l;
			if (implode($board[$l][3])=="xxxxx") $found=$l;
			if (implode($board[$l][4])=="xxxxx") $found=$l;
			if ($board[$l][0][0].$board[$l][1][0].$board[$l][2][0].$board[$l][3][0].$board[$l][4][0]=="xxxxx") $found=$l;
			if ($board[$l][0][1].$board[$l][1][1].$board[$l][2][1].$board[$l][3][1].$board[$l][4][1]=="xxxxx") $found=$l;
			if ($board[$l][0][2].$board[$l][1][2].$board[$l][2][2].$board[$l][3][2].$board[$l][4][2]=="xxxxx") $found=$l;
			if ($board[$l][0][3].$board[$l][1][3].$board[$l][2][3].$board[$l][3][3].$board[$l][4][3]=="xxxxx") $found=$l;
			if ($board[$l][0][4].$board[$l][1][4].$board[$l][2][4].$board[$l][3][4].$board[$l][4][4]=="xxxxx") $found=$l;
			if ($found != -1) $result=$sums[$found]*$draws[$k];
		}
	}


}
echo "Result: ".$result;
?>
