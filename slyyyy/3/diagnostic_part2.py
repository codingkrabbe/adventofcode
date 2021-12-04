import os, sys, math, copy

def main():
	def common(lines, bit, sign):
		summ = 0
		for l in lines:
			summ += int(l[bit])

		if(summ > len(lines) / 2):
			return 1
		if(summ == len(lines) / 2):
			if(sign == "MOST"): return 1
			if(sign == "LEAST"): return 0
		else:
			return 0

	def find_significant_number(lines, sign):
		bit = 0
		while(len(lines) > 1):
			i = 0
			b_criteria = common(lines, bit, sign)
			
			while(i < len(lines)):
				#if((b_criteria == 1 and int(lines[i][bit]) == 0) or
				#   (b_criteria == 0 and int(lines[i][bit]) == 1)):				

				if((sign == "MOST" and b_criteria == 1 and int(lines[i][bit]) == 0) or
				   (sign == "MOST" and b_criteria == 0 and int(lines[i][bit]) == 1) or
				   (sign == "LEAST" and b_criteria == 1 and int(lines[i][bit]) == 1) or
				   (sign == "LEAST" and b_criteria == 0 and int(lines[i][bit]) == 0)):
					
					#print(str(len(lines)) + " " + str(i) + " " + str(bit) + " " + str(b_criteria) + " " + lines[i][:-1])
					#if(i > 5): break;
					#print(lines)
					lines.pop(i)
				else:
					i += 1		
			bit += 1
		
		print("---------------------------------------")
		return lines[0]

	with open("input.txt", 'r') as file:
		lines = file.readlines();
		num_bits = len(lines[0])-1
		digits = [0]*(num_bits)
		

		print(digits)

		oxygen_generator_rating = find_significant_number(copy.copy(lines), "MOST")
		co2_scrubber_rating = find_significant_number(lines, "LEAST")

		print("oxygen (binary): " + str(oxygen_generator_rating[:-1]))
		print("CO2 (binary): " + str(co2_scrubber_rating[:-1]))
		print("oxygen (decimal): " + str(int(oxygen_generator_rating[:-1],2)))
		print("CO2 (decimal): " + str(int(co2_scrubber_rating[:-1],2)))

		print("life support rating: " + str(int(oxygen_generator_rating[:-1],2)*int(co2_scrubber_rating[:-1],2)))


if __name__ == "__main__":
	sys.exit(main())