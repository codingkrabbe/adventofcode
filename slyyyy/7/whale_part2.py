import os, sys, math

def gauss(n):
	fact = 0
	
	for i in range(1,n+1):
		fact = fact + i
	return fact


def main():
	crab_list = None
	with open("input.txt", 'r') as file:
		crab_list = [int(x) for x in file.readline().split(",")]
	
	fuel = [0]*(max(crab_list)+1)

	for i in range(len(fuel)):	
		for j in range(len(crab_list)):
			if(i == crab_list[j]):
				continue
			else:
				fuel[i] += gauss(abs(i-crab_list[j]))
	
	print("Minimum required fuel: " + str(min(fuel)))


if __name__ == "__main__":
	sys.exit(main())

