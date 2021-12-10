import os, sys, math

neighbours = [(0,-1), (1,0), (0,1), (-1,0)]

def calc_basin_recursive(coord, mapp, covered_list):
	summ = 0
	for n in neighbours:
		if(coord[0]+n[0] >= 0 and coord[0]+n[0] < len(mapp[coord[1]]) and
		   coord[1]+n[1] >= 0 and coord[1]+n[1] < len(mapp)):
			# only inspect if value is higher but not 9
			if(mapp[coord[1]][coord[0]] < mapp[coord[1]+n[1]][coord[0]+n[0]] and
			   mapp[coord[1]+n[1]][coord[0]+n[0]] < 9):
				new_coord = (coord[0]+n[0], coord[1]+n[1])
				# only inspect coordinate if it wasn't already inspected in a different branch
				if(not new_coord in covered_list):
					covered_list.append(new_coord)
					summ += calc_basin_recursive(new_coord, mapp, covered_list) + 1
	return summ


def main():
	input_values = []
	lows = []
	basin_list = []
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			input_values.append([int(x) for x in line if(x !='\n')])
	
	# calculate lows
	for i in range(len(input_values)):
		for j in range(len(input_values[i])):
			summ = 0
			count = 0
			for n in neighbours:
				if(j+n[0] >= 0 and j+n[0] < len(input_values[i]) and
				   i+n[1] >= 0 and i+n[1] < len(input_values)):
					if(input_values[i][j] < input_values[i+n[1]][j+n[0]]):
						summ += 1
					count += 1
			if(summ == count):
				lows.append((j,i))

	# calculate basins based on lows
	for p in lows:
		covered_list = [p] # add already inspected coords to prevent adding duplicates to basin
		basin_list.append(1 + calc_basin_recursive(p, input_values, covered_list))

	basin_list.sort()
	result = basin_list[len(basin_list)-1] * basin_list[len(basin_list)-2] * basin_list[len(basin_list)-3]

	print("Sum of Risk Levels: " + str(result))


if __name__ == "__main__":
	sys.exit(main())

