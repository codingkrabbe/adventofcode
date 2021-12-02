import os, sys

def main():
	with open("input.txt", 'r') as file:
		x = 0; y = 0; aim = 0; direction = file.readline();
		while(direction != ""):
			dir_l = direction.split()
			match dir_l[0]:
				case "forward": x += int(dir_l[1]); y += (aim*int(dir_l[1])); 
				case "up":      aim -= int(dir_l[1]);
				case "down":    aim += int(dir_l[1]);
			direction = file.readline()
		print("location: " + str(x*y))


if __name__ == "__main__":
	sys.exit(main())