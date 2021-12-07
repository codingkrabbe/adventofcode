import os, sys, math

def faculty(n):
	fact = 1
	
	for i in range(1,n+1):
		fact = fact + i
	return fact


def calc_shortest_recursive(i_list):
	if(len(i_list) == 1):
		return i_list
	if(len(i_list) == 2):
		diff = faculty(abs(i_list[0]-i_list[1]))
		return [diff,diff]
		
	l_left = i_list[0:math.ceil(len(i_list)/2)]
	l_right = i_list[math.ceil(len(i_list)/2):len(i_list)]

	left  = calc_shortest_recursive(l_left)
	right = calc_shortest_recursive(l_right)

	fuel_costs = left + right

	for i in range(len(fuel_costs)):
		if(i < len(l_left)):
			for j in range(len(l_right)):
				fuel_costs[i] += faculty(abs(l_right[j]-l_left[i])) 
		else:
			for j in range(len(l_left)):
				fuel_costs[i] += faculty(abs(l_right[i-len(l_left)]-l_left[j]))

	print(fuel_costs)

	return fuel_costs


def main():
	crab_list = None
	with open("input.txt", 'r') as file:
		crab_list = [int(x) for x in file.readline().split(",")]

	print(calc_shortest_recursive(crab_list))
	print("Minimum required fuel: " + str(min(calc_shortest_recursive(crab_list))))


if __name__ == "__main__":
	sys.exit(main())


"""def calc_shortest_recursive(i_list, depth):
	if(len(i_list) == 1):
		return {"list": i_list, "depth" : depth, "max_depth" : depth }
	if(len(i_list) == 2):
		diff = abs(i_list[0]-i_list[1])
		return {"list": [diff,diff], "depth" : depth-1, "max_depth" : depth }
		
	l_left = i_list[0:math.ceil(len(i_list)/2)]
	l_right = i_list[math.ceil(len(i_list)/2):len(i_list)]

	left  = calc_shortest_recursive(l_left, depth+1)
	right = calc_shortest_recursive(l_right, depth+1)

	fuel_costs = left["list"] + right["list"]

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

	print("Minimum required fuel: " + str(min(calc_shortest_recursive(crab_list, 0))))


	#print("Total Fish Population: " + str(len(fish_list)))


if __name__ == "__main__":
	sys.exit(main())"""