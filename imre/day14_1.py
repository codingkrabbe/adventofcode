import re
import numpy as np
# parsing input
lines = open('input_example.txt', 'r').readlines()
polymer = lines[0].strip()
rules = {}
letter_frequency = {}
for line in lines[2:]:
    a = line.strip().split(' -> ')
    rules[a[0]] = {'sub': a[1], 'regex': r'(?=(' + a[0] + '))'}
    for c in list(a[0]) + [a[1]]:
        if c not in letter_frequency:
            letter_frequency[a[1]] = 0


def iterate(poly, rule_set):
    occurrences = {}
    insert_cont = 0
    for r in rule_set.keys():
        occurrences[r] = [m.start() + 1 for m in re.finditer(rule_set[r]['regex'], poly)]
        insert_cont += len(occurrences[r])
    shift_registry = np.zeros((len(poly) + insert_cont), dtype='int32')
    for r in rule_set.keys():
        for o in occurrences[r]:
            poly = poly[:o + shift_registry[o]] + rule_set[r]['sub'] + poly[o + shift_registry[o]:]
            shift_registry[o:] += 1
    return poly


for i in range(10):
    polymer = iterate(polymer, rules)
    print(len(polymer))
for l in letter_frequency.keys():
    letter_frequency[l] = len([m.start() + 1 for m in re.finditer(l, polymer)])
print('---')
print(max([letter_frequency[k] for k in letter_frequency.keys()]) -
      min([letter_frequency[k] for k in letter_frequency.keys()]))
