<?php
$input=file("input_5_1.txt");
$found=0;
$grid=array_fill(0,1000,array_fill(0,1000,0));

for ($i=0; $i<count($input); $i++) {
	$data=explode(",",str_replace(" -> ",",",trim($input[$i])));
	if ($data[0]==$data[2]) {
		if ($data[1]<$data[3]) {
			for ($j=$data[1];$j<=$data[3];$j++) {
				$grid[$j][$data[0]]+=1;
			}
		} else {
			for ($j=$data[3];$j<=$data[1];$j++) {
                                $grid[$j][$data[0]]+=1;
                        }
		}
	}
	if ($data[1]==$data[3]) {
		if ($data[0]<$data[2]) {
			for ($j=$data[0];$j<=$data[2];$j++) {
                	        $grid[$data[1]][$j]+=1;
                	}
		} else {
			for ($j=$data[2];$j<=$data[0];$j++) {
                        	$grid[$data[1]][$j]+=1;
                	}
		}
	}
}

for ($i=0;$i<count($grid);$i++) {
	for ($j=0;$j<count($grid[$i]);$j++) {
		if ($grid[$i][$j]>=2) $found++;
	}
}
echo "Result: $found";
?>
