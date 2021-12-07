import os, sys


def main():
	fish_list = None
	with open("input.txt", 'r') as file:
		fish_list = [int(x) for x in file.readline().split(",")]


	num_days = 80

	for d in range(num_days):
		for i in range(len(fish_list)):
			if(fish_list[i] == 0):
				fish_list[i] = 6
				fish_list.append(8)
			else:
				fish_list[i] -= 1

	print("Total Fish Population: " + str(len(fish_list)))


if __name__ == "__main__":
	sys.exit(main())