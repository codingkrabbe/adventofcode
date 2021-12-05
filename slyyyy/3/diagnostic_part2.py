import os, sys, math, copy

def main():
	def common(lines, bit):
		summ = 0
		for l in lines:
			summ += int(l[bit])
		if(summ >= len(lines) / 2):
			return 1
		else:
			return 0

	def find_significant_number(lines, sign):
		bit = 0
		while(len(lines) > 1):
			i = 0
			b_criteria = common(lines, bit)
			
			while(i < len(lines)):		
				if((sign == "MOST" and b_criteria == 1 and int(lines[i][bit]) == 0) or
				   (sign == "MOST" and b_criteria == 0 and int(lines[i][bit]) == 1) or
				   (sign == "LEAST" and b_criteria == 1 and int(lines[i][bit]) == 1) or
				   (sign == "LEAST" and b_criteria == 0 and int(lines[i][bit]) == 0)):
					lines.pop(i)
				else:
					i += 1		
			bit += 1
		
		return lines[0]

	with open("input.txt", 'r') as file:
		lines = file.readlines();
		num_bits = len(lines[0])-1
		digits = [0]*(num_bits)

		oxygen_generator_rating = find_significant_number(copy.copy(lines), "MOST")
		co2_scrubber_rating = find_significant_number(lines, "LEAST")

		print("life support rating: " + str(int(oxygen_generator_rating[:-1],2)*int(co2_scrubber_rating[:-1],2)))


if __name__ == "__main__":
	sys.exit(main())