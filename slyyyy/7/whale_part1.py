import os, sys, math


def calc_shortest_recursive(i_list):
	if(len(i_list) == 1):
		return i_list
	if(len(i_list) == 2):
		diff = abs(i_list[0]-i_list[1])
		return [diff,diff]
		
	l_left = i_list[0:math.ceil(len(i_list)/2)]
	l_right = i_list[math.ceil(len(i_list)/2):len(i_list)]

	left  = calc_shortest_recursive(l_left)
	right = calc_shortest_recursive(l_right)

	fuel_costs = left + right

	for i in range(len(fuel_costs)):
		if(i < len(l_left)):
			for j in range(len(l_right)):
				fuel_costs[i] += abs(l_right[j]-l_left[i]) 
		else:
			for j in range(len(l_left)):
				fuel_costs[i] += abs(l_right[i-len(l_left)]-l_left[j])

	return fuel_costs




def main():
	crab_list = None
	with open("input.txt", 'r') as file:
		crab_list = [int(x) for x in file.readline().split(",")]

	print("Minimum required fuel: " + str(min(calc_shortest_recursive(crab_list))))

if __name__ == "__main__":
	sys.exit(main())