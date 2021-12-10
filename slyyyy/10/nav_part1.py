import os, sys, math

open_bracket_types = ['(','[','{','<']
close_bracket_types = [')',']','}','>']

scores = [3, 57, 1197, 25137]

def main():
	illegals = [0,0,0,0]
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			stack = []
			for i in range(len(line)):
				if(line[i] in open_bracket_types):
					stack.append(line[i])
				if(line[i] in close_bracket_types):
					index = close_bracket_types.index(line[i])
					if(stack.pop() != open_bracket_types[index]):
						illegals[index] += 1

	result = 0
	for i in range(len(illegals)):
		result += illegals[i]*scores[i] 

	print("Syntax Error Score: " + str(result))


if __name__ == "__main__":
	sys.exit(main())

