import os, sys, math
from itertools import permutations


num_segments_per_digit = { "1" : 2, "4": 4, "7": 3, "8": 7 }


def match_num_characters(signal_a, signal_b):
	sum = 0
	for c in signal_a:
		if(c in signal_b): sum += 1
	return sum


def check_all_permutations(signal, output):
	perms = [''.join(p) for p in permutations(signal)]

	for p in perms:
		if p == output:
			return True

	return False


def decode_signal_input(signals):
	signals.sort(key=len) # sort list based on length of signals

	segments = dict()

	segments["1"] = signals[0]
	segments["7"] = signals[1]
	segments["4"] = signals[2]
	segments["8"] = signals[9]

	segments["2"] = None
	segments["3"] = None
	segments["5"] = None

	segments["0"] = None
	segments["6"] = None
	segments["9"] = None

	# determine 2, 3 and 5
	i = 3
	while(i <= 5):
		if(segments["2"] == None 
			and segments["3"] != None
			and segments["5"] != None 
			and signals[i] != segments["3"]
			and signals[i] != segments["5"]):
			segments["2"] = signals[i]

		if(segments["3"] == None 
			and match_num_characters(signals[i], segments["4"]) == 3
			and match_num_characters(signals[i], segments["1"]) == 2):
			segments["3"] = signals[i]


		if(segments["5"] == None 
			and segments["3"] != None
			and signals[i] != segments["3"]
			and match_num_characters(signals[i], segments["4"]) == 3):
			segments["5"] = signals[i]


		if((segments["2"] == None 
			or segments["3"] == None 
			or segments["5"] == None) 
			and i == 5):
			i = 3
			continue

		i += 1

	# determine 0, 6 and 9
	i = 6
	while(i <= 8):
		if(segments["0"] == None
			and segments["6"] != None
			and segments["9"] != None
			and signals[i] != segments["6"]
			and signals[i] != segments["9"]
			and match_num_characters(signals[i], segments["8"]) == 6):
			segments["0"] = signals[i]

		if(segments["6"] == None
			and segments["9"] != None
			and signals[i] != segments["9"] 
			and match_num_characters(signals[i], segments["5"]) == 5):
			segments["6"] = signals[i]

		if(segments["9"] == None
			and match_num_characters(signals[i], segments["4"]) == 4):
			segments["9"] = signals[i]


		if((segments["0"] == None 
			or segments["6"] == None 
			or segments["9"] == None) 
			and i == 8):
			i = 6
			continue

		i += 1


	#print(segments)

	return segments
	# TODO return result


def decode_and_calc_output_digits(segments, digits):
	summ = ""
	for d in digits:
		for k in segments.keys():
			if check_all_permutations(segments[k], d) == True:
				summ += k

	return int(summ)


def main():
	input_values = { "signals" : [], "digits" : []}
	with open("input.txt", 'r') as file:
		for line in file.readlines():
			index = line.find("|")
			
			input_values["signals"].append(line[0:index].split())
			input_values["digits"].append(line[index+1:len(line)-1].split())
	
	summ = 0
	for i in range(len(input_values["signals"])):
		segments = decode_signal_input(input_values["signals"][i])
		sum_output = decode_and_calc_output_digits(segments, input_values["digits"][i])

		summ += sum_output

		"""# TEST # 
		for j in range(len(segments)):
			for k in range(j+1,len(segments)):
				print(segments[str(j)] + " | " + segments[str(k)])
				if(segments[str(j)] == segments[str(k)]):
					print("ERROR")

		return
		# END OF TEST #"""
	
	print("Number of Digit Appearance: " + str(summ))


if __name__ == "__main__":
	sys.exit(main())

