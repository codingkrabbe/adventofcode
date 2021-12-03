import pyperclip
input = pyperclip.paste().splitlines()
ones = [0] * len(input[0]) # Number of ones
for i in input:
    vals = [int(n) for n in i]
    ones = [a + b for a, b in zip(ones, vals)]
bin1 = [int(n > len(input) / 2) for n in ones] # Most common digit
bin2 = [{0: 1, 1: 0}[n] for n in bin1] # Mirror the above
gamma = sum([n * pow(2, len(bin1) - j - 1) for j, n in enumerate(bin1)]) # Convert to decimal
epsilon = sum([n * pow(2, len(bin1) - j - 1) for j, n in enumerate(bin2)]) # Convert to decimal
print(gamma,epsilon,gamma*epsilon)
