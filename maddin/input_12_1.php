<?php
$input=file("input_12_1.txt");
$result=0;
$paths=[];
$caves=[];

function follow($key,$caves,$x) {
global $paths;
	if ($key != "end") {
		for ($i=2; $i<count($paths[$key]);$i++) {
			if ($paths[$key][$i] != "start") {
				if ($paths[$paths[$key][$i]][0] == 0 || strpos($caves[$x],$paths[$key][$i]) < 1) {
					$c=count($caves);
					if ($paths[$paths[$key][$i]][0] == 0 || $paths[$key][$i] == "end") $caves[$c]=$caves[$x].",".$paths[$key][$i];
					if ($paths[$paths[$key][$i]][0] == 1 && $paths[$key][$i] != "end") $caves[$c]=$caves[$x].",SMALL,".$paths[$key][$i];
					$caves=follow($paths[$key][$i],$caves,$c);
				}
			}
		}
	}

return $caves;
}


for ($i=0;$i<count($input);$i++) {
	$data=explode("-",trim($input[$i]));
	if (!array_key_exists($data[0],$paths)) {
		$paths[$data[0]]=[];
		$paths[$data[0]][0]=0;
		$paths[$data[0]][1]=0;
		if (strtolower($data[0]) == $data[0]) $paths[$data[0]][0]=1;
	}
	$paths[$data[0]][count($paths[$data[0]])]=$data[1];
	if (!array_key_exists($data[1],$paths)) {
		$paths[$data[1]]=[];
                $paths[$data[1]][0]=0;
                $paths[$data[1]][1]=0;
                if (strtolower($data[1]) == $data[1]) $paths[$data[1]][0]=1;
	}
	$paths[$data[1]][count($paths[$data[1]])]=$data[0];
}

$caves[0]="start";
$caves=follow("start",$caves,0);

for ($i=0;$i<count($caves);$i++) {
	if (strpos($caves[$i],"end") && strpos($caves[$i],"SMALL")) $result+=1;
}

echo "Result: $result";

?>
