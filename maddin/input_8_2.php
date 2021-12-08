<?php
$input=file("input_8_1.txt");
$results=0;
$numbers=array_fill(0,count($input),array_fill(0,10,0));

function decode($in,$digits,$raw) {
	$result=array_fill(0,count($in),0);
        for ($j=0;$j<count($raw);$j++) {
                if (strlen($raw[$j])==2) $digits[1]=$raw[$j];
                if (strlen($raw[$j])==3) $digits[7]=$raw[$j];
                if (strlen($raw[$j])==4) $digits[4]=$raw[$j];
	}
        for ($j=0;$j<count($raw);$j++) {
		 if (strlen($raw[$j])==5) {
                 	if (strlen(str_replace(str_split($digits[1]),["",""],$raw[$j]))==3) {
                        	        $digits[3]=$raw[$j];
                        	} else if (strlen(str_replace(str_split($digits[4]),["",""],$raw[$j]))==2) {
                                        $digits[2]=$raw[$j];
                                }
                }
        }
	for ($j=0;$j<count($in);$j++) {
		if (strlen($in[$j])==2) $result[$j]=1;
		if (strlen($in[$j])==3) $result[$j]=7;
		if (strlen($in[$j])==4) $result[$j]=4;
		if (strlen($in[$j])==7) $result[$j]=8;
		if (strlen($in[$j])==5) {
			if (strlen(str_replace(str_split($digits[1]),["",""],$in[$j]))==3) {
				$result[$j]=3;
				$digits[3]=$in[$j];
			}
		        if ($result[$j]!=3) if (strlen(str_replace(str_split($digits[4]),["","","",""],$in[$j]))==2) {
                                $result[$j]=5;
                        }
			 if (strlen(str_replace(str_split($digits[4]),["","","",""],$in[$j]))==3) {
                                $result[$j]=2;
                        }
			if (strlen(str_replace(str_split($digits[3]),["","","","",""],$in[$j]))==2) {
                                $result[$j]=3;
                        }
		}
		if (strlen($in[$j])==6) {
		        if (strlen(str_replace(str_split($digits[1]),["",""],$in[$j]))==5) {
                        	$result[$j]=6;
                	}
			if (strlen(str_replace(str_split($digits[1]),["",""],$in[$j]))==4) {
  	                	if (strlen(str_replace(str_split($digits[3]),["","","","",""],$in[$j]))==1) {
					$result[$j]=9;
				} else $result[$j]=0;
                       }

		}
	}
	return $result;
}

for ($i=0;$i<count($input);$i++) {
	$data=explode(" | ",trim($input[$i]));
	$segments=explode(" ",$data[1]);
	for ($j=0;$j<count($segments);$j++) {
		if (strlen($segments[$j])==2) $numbers[$i][1]=$segments[$j];
		if (strlen($segments[$j])==3) $numbers[$i][7]=$segments[$j];
		if (strlen($segments[$j])==4) $numbers[$i][4]=$segments[$j];
		if (strlen($segments[$j])==7) $numbers[$i][8]=$segments[$j];
	}
	$results+=implode(decode($segments,$numbers[$i],explode(" ",str_replace(" |","",trim($input[$i])))));
}

echo "Result: ".$results;
?>
