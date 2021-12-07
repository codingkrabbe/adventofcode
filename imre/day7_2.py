import sys
p = [int(n) for n in open('input.txt', 'r').readline().split(',')]
min_val = sys.maxsize
min_idx = -1


# Very slow. Should build dict first probably
def fuel_for_step(step):
    return step + sum(list(range(step)))


for i in range(len(p)):
    curr_fuel = sum([fuel_for_step(abs(n - p[i])) for n in p])
    if curr_fuel < min_val:
        min_val = curr_fuel
        min_idx = i
print(min_val, min_idx)
