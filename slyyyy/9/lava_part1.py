import os, sys, math

neighbours = [(0,-1), (-1,0), (1,0), (0,1)]

def main():
	input_values = []
	lows = []
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			input_values.append([int(x) for x in line if(x !='\n')])
			
	#print(input_values)
	
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
				lows.append(input_values[i][j])

	result = sum(lows) + len(lows)
	
	print("Sum of Risk Levels: " + str(result))


if __name__ == "__main__":
	sys.exit(main())

