lines = open('input.txt', 'r').readlines()
gamma, epsilon = '', ''
zeros, ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in lines:
    for idx, char in enumerate(line):
        if char == '0':
            zeros[idx] += 1
        elif char != '\n':
            ones[idx] += 1
for i in range(len(zeros)):
    if zeros[i] > ones[i]:
        gamma, epsilon = gamma + '0', epsilon + '1'
    else:
        gamma, epsilon = gamma + '1', epsilon + '0'
print(int(gamma, 2) * int(epsilon, 2))