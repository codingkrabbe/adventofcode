<?php
$input=file("input_14_1.txt");
$rules=[];
$items=[];
$rank=[];
$comb=[];
$comb_n=[];
$comb_add=[];

$polymer=str_split(trim($input[0]));
for ($j=0;$j<count($polymer);$j++) {
        $items[$polymer[$j]]=0;
}
for ($i=2;$i<count($input);$i++) {
	$rule=explode(" ",trim($input[$i]));
	$rules[$rule[0]]=$rule[2];
	$items[$rule[2]]=0;
	$comb[$rule[0]]=0;
	$rank[0]=$rule[2];
	$rank[1]=$rule[2];
}
$comb_n=$comb;
for ($j=0;$j<count($polymer)-1;$j++) {
	$comb[$polymer[$j].$polymer[$j+1]]+=1;
}
for ($j=0;$j<40;$j++) {
	$comb_add=$comb_n;
	foreach ($comb as $poly => $iters) {
		$combo=str_split($poly);
		array_splice($combo,1,0,$rules[$poly]);
		$items[$rules[$poly]]+=$iters;
		for ($k=0;$k<count($combo)-1;$k++) {
                	$comb_add[$combo[$k].$combo[$k+1]]+=$iters;
        	}
	}
	$comb=$comb_add;
}
for ($j=0;$j<count($polymer);$j++) {
      $items[$polymer[$j]]+=1;
}
foreach ($items as $item => $amount) {
        if ($amount > $items[$rank[1]]) $rank[1]=$item;
	if ($amount < $items[$rank[0]]) $rank[0]=$item;
}
$result=$items[$rank[1]]-$items[$rank[0]];
echo "Result: ".$result;
?>
