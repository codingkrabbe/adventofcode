import os, sys, math


digits_mapping = { "1" : 2, "4": 4, "7": 3, "8": 7 }

def main():
	input_values = { "signals" : [], "digits" : []}
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			index = line.find("|")
			
			input_values["signals"].append(line[0:index].split())
			input_values["digits"].append(line[index+1:len(line)-1].split())
	
	sum = 0
	for l in input_values["digits"]:
		for d in l:
			if(len(d) in digits_mapping.values()):
				sum += 1

	#print(input_values)
	
	print("Number of Digit Appearance: " + str(sum))


if __name__ == "__main__":
	sys.exit(main())

