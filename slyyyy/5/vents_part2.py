import os, sys


def parseLine(line):
	split_index = line.find('->')

	xy1 = line[0:split_index-1].split(",")
	xy2 = line[split_index+3:len(line)-1].split(",")

	return { "xy_start": xy1, "xy_end": xy2}

def main():
	size = 1000
	mapp = [[]]*size
	danger_points = []

	for i in range(len(mapp)):
		mapp[i] = [0]*size

	with open("input.txt", 'r') as file:
		line = file.readline()
		while(line != ""):
			coords = parseLine(line)
			
			y_start = int(coords["xy_start"][1])
			y_end = int(coords["xy_end"][1])
			x_start = int(coords["xy_start"][0])
			x_end = int(coords["xy_end"][0])
			
			if(y_start != y_end and x_start != x_end):
				x = x_start; y = y_start
				x_sign = 1; y_sign = 1
				
				if(x_end-x_start < 0): x_sign = -1
				if(y_end-y_start < 0): y_sign = -1

				for i in range(abs(y_end-y_start)+1):
					mapp[y_start+i*y_sign][x_start+i*x_sign] += 1
			else:
				if(y_start > y_end): y_start, y_end = y_end, y_start
				if(x_start > x_end): x_start, x_end = x_end, x_start

				for y in range(y_start, y_end+1):
					for x in range(x_start, x_end+1):
						mapp[y][x] += 1

			line = file.readline();

	for y in range(len(mapp)):
		for x in range(len(mapp[y])):
			if(mapp[y][x] >= 2):
				danger_points.append((x,y))

	print("Total Overlaps: " + str(len(danger_points)))

		


if __name__ == "__main__":
	sys.exit(main())