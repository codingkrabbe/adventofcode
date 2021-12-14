lines = open('input.txt', 'r').readlines()
polymer = lines[0].strip()
rules = {}
letter_combinations = {}
letter_frequency = {}
# parsing input
for line in lines[2:]:
    a = line.strip().split(' -> ')
    rules[a[0]] = a[1]
    for c in list(a[0]) + [a[1]]:
        if c not in letter_frequency:
            letter_frequency[a[1]] = 0
for l1 in letter_frequency.keys():
    for l2 in letter_frequency.keys():
        letter_combinations[l1 + l2] = 0

# Init population
for i in range(len(polymer)-1):
    letter_combinations[polymer[i:i+2]] += 1


def iterate(combos, rule_set):
    # reset dict
    combos_out = combos.copy()
    for c in combos_out.keys():
        combos_out[c] = 0
    # Generate next population based on the rules
    for r in rule_set:
        combos_out[r[0] + rule_set[r]] += combos[r]
        combos_out[rule_set[r] + r[1]] += combos[r]
    return combos_out


# Do iterations
for i in range(40):
    letter_combinations = iterate(letter_combinations, rules)
# Calculate frequencies of letters
letter_frequency[polymer[-1]] = 1 # The last character stay last, and should be corrected
for l in letter_frequency.keys():
    for c in letter_combinations.keys():
        if l == c[0]:
            letter_frequency[l] += letter_combinations[c]

print(max([letter_frequency[k] for k in letter_frequency.keys()]) -
      min([letter_frequency[k] for k in letter_frequency.keys()]))
