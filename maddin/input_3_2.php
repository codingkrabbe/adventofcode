<?php
$input=file("input_3_1.txt");


function get_bit($input,$pos) {
        $output0=0;
        $output1=0;

        for ($i=0; $i<count($input); $i++) {
                $itemp=str_split($input[$i]);
                        if ($itemp[$pos]=="0") $output0+=1;
                        if ($itemp[$pos]=="1") $output1+=1;
        }
        $i=0;
        $output="1";
        if ($output0>$output1) $output="0";
        return $output;
}

function get_bin($input,$nbit) {
        $outlist=$input;
        for ($i=0; $i<count(str_split($input[0])); $i++) {
                $bit=get_bit($outlist,$i);
                if ($nbit==0) $bit=abs($bit-1);
                $k=0;
                $templist=[];
                for ($j=0; $j<count($outlist); $j++) {
                        $tempbit=str_split($outlist[$j]);
                        if ($tempbit[$i]==$bit) {
                                $templist[$k]=$outlist[$j];
                                $k++;
                        }
                }
                if (count($templist)>0) $outlist=$templist;
        }
        return implode($outlist);
}


$ox=get_bin($input,"1");
$co2=get_bin($input,"0");

echo (bindec($ox)*bindec($co2));

?>
