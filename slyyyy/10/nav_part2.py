import os, sys, math

open_bracket_types = ['(','[','{','<']
close_bracket_types = [')',']','}','>']

scores = [1, 2, 3, 4]

def main():
	completions = []
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			incomplete = False
			stack = []
			for i in range(len(line)):
				if(line[i] in open_bracket_types):
					stack.append(line[i])
				if(line[i] in close_bracket_types):
					index = close_bracket_types.index(line[i])
					if(stack.pop() != open_bracket_types[index]):
						incomplete = True
						break
			if(len(stack) > 0 and incomplete == False):
				l_completion = []
				while(len(stack) > 0):
					c = stack.pop()
					index = open_bracket_types.index(c)
					l_completion.append(close_bracket_types[index])
				completions.append(l_completion)

	# calculate scores
	result = []
	for i in range(len(completions)):
		temp_score = 0
		for c in completions[i]:
			index = close_bracket_types.index(c)
			temp_score = temp_score*5 + scores[index]
		result.append(temp_score)

	result.sort()

	for i in range(len(result)):
		print(str(i) + ": " + str(result[i]))

	print("Syntax Error Score: " + str(result[math.floor(len(result)/2)]))


if __name__ == "__main__":
	sys.exit(main())

