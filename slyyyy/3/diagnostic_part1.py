import os, sys, math

def main():
	def most_common(sum, num_items):
		if(sum > num_items / 2):
			return 1
		else:
			return 0

	def calc_gamma_rate(digits, num_items, num_bits):
		gamma_rate = 0
		for i in range(num_bits):
			gamma_rate += math.pow(2,i)*most_common(digits[num_bits-i-1], num_items)
		return int(gamma_rate)

	with open("input.txt", 'r') as file:
		lines = file.readlines();
		num_bits = len(lines[0])-1
		digits = [0]*(num_bits)
		for l in lines:
			for i in range(num_bits):
				digits[i] += int(l[i])
				
		gamma_rate = calc_gamma_rate(digits, len(lines), num_bits)
		epsilon_rate = int(math.pow(2,num_bits)-1-gamma_rate)

		print("location: " + str(epsilon_rate*gamma_rate))


if __name__ == "__main__":
	sys.exit(main())