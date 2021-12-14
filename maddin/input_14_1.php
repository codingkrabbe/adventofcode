<?php
$input=file("input_14_1_t.txt");
$rules=[];
$items=[];
$rank=[];

$polymer=str_split(trim($input[0]));

for ($i=2;$i<count($input);$i++) {
	$rule=explode(" ",trim($input[$i]));
	$rules[$rule[0]]=$rule[2];
	$items[$rule[2]]=0;
	$rank[0]=$rule[2];
	$rank[1]=$rule[2];
}

for ($step=0;$step<10;$step++) {

	for ($j=0;$j<count($polymer)-1;$j+=2) {
		array_splice($polymer,$j+1,0,$rules[$polymer[$j].$polymer[$j+1]]);
	}

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
