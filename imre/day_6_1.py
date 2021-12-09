def iterate(pop):
    p = pop.copy()
    for i in range(8):
        p[i] = pop[i + 1]
    p[8] = pop[0]
    p[6] += pop[0]
    return p


pop = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
population = [int(n) for n in open('input.txt', 'r').readline().split(',')]
for fish in population:
    pop[fish] += 1

for i in range(80):
    pop = iterate(pop)

print(sum(pop.values()))
