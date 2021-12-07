import sys
p = [int(n) for n in open('input.txt', 'r').readline().split(',')]
min_val = sys.maxsize
min_idx = -1
for i in range(len(p)):
    curr_fuel = sum([abs(n - p[i]) for n in p])
    if curr_fuel < min_val:
        min_val = curr_fuel
        min_idx = i
print(min_val, min_idx)