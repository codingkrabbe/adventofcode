import os, sys

def main():
	with open("input.txt", 'r') as file:
		inc = 0; first = file.readline();
		try:
			while(first != ""):
				second = file.readline()
				if(int(second) > int(first)): inc += 1;
				first = second
		except:
			pass
		print("the number of times a depth measurement increases: " + str(inc))


if __name__ == "__main__":
	sys.exit(main())