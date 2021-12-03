import os, sys

def main():
	with open("input.txt", 'r') as file:
		inc = 0; t1 = (int(file.readline()), int(file.readline()), int(file.readline()));
		try:
			while(not "" in t1):
				t2 = (int(t1[1]), int(t1[2]), int(file.readline()));
				if(sum(t2) > sum(t1)): inc += 1;
				t1 = t2
		except:
			pass
		print("the number of times a depth measurement increases: " + str(inc))


if __name__ == "__main__":
	sys.exit(main())