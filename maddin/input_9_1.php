<?php
$input=file("input_9_1.txt");
$data=array_fill(0,count($input),array_fill(0,strlen(trim($input[0])),"x"));
$result=0;

for ($i=0;$i<count($input);$i++) {
	$row=str_split(trim($input[$i]));
	for ($j=0;$j<count($row);$j++) {
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
		if ($data[$i][$j]!="x") $result+=$data[$i][$j]+1;
	}
}

echo "Result: $result";

?>
