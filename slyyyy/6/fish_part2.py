import os, sys


def main():
	fish_max_days = 9
	num_days = 256
	fish_input = None
	
	with open("input.txt", 'r') as file:
		fish_input = [int(x) for x in file.readline().split(",")]

	fish_list = [0]*fish_max_days

	for i in range(fish_max_days):
		for j in fish_input:
			if(j == i): fish_list[i] += 1

	for d in range(num_days):
		num_new_fish = fish_list[0]
		for i in range(fish_max_days-1):
			fish_list[i] = fish_list[i+1]
		fish_list[8] = num_new_fish
		fish_list[6] += num_new_fish

	print("Total Fish Population: " + str(sum(fish_list)))


if __name__ == "__main__":
	sys.exit(main())