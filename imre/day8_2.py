def decode_wiring(code_list):
    # First collect known digits
    mapping = {'a': {}, 'b': {}, 'c': {}, 'd': {}, 'e': {}, 'f': {}, 'g': {}}
    in_one = in_four = in_seven = set()
    for a in code_list:
        if len(a) == 2 and not in_one:
            in_one = set(a)
        if len(a) == 3 and not in_seven:
            in_seven = set(a)
        if len(a) == 4 and not in_four:
            in_four = set(a)
    if not (in_one and in_four and in_seven):
        print("Not enough info")
        return mapping
    # Then, lets find known mappings
    mapping['a'] = in_seven - in_one
    # Now, 6 is the only 6 segment digit, that has 2 intersections with 7
    for a in code_list:
        aa = set(a)
        if len(aa) == 6 and len(in_seven.intersection(aa)) == 2:
            # this is a 6. It has excately one intersection with 1
            mapping['f'] = aa.intersection(in_one)
    mapping['c'] = in_one - mapping['f']
    # Now let's look for 3
    for a in code_list:
        aa = set(a)
        if len(aa) == 5 and len(aa.intersection(in_seven)) == 3:
            # This is a 3
            mapping['d'] = (aa - in_seven).intersection(in_four)
            mapping['g'] = aa - in_seven - in_four
    in_three = mapping['a'] | mapping['c'] | mapping['d'] | mapping['f'] | mapping['g']
    # Now let's look for 9
    for a in code_list:
        aa = set(a)
        if len(aa) == 6 and len(aa - in_three) == 1:
            # This is a 9
            mapping['b'] = aa - in_three
    # Find the missing one from 8
    for a in code_list:
        aa = set(a)
        if len(aa) == 7:
            # This is a 8
            mapping['e'] = aa - in_three - mapping['b']
    return mapping


def string_to_digit(string, mapping):
    code_table = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
                  'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
    reverse_mapping = {}
    for k in mapping.keys():
        reverse_mapping[list(mapping[k])[0]] = k
    code_list = [reverse_mapping[c][0] for c in string]
    code_list.sort()
    code_string = ''.join(code_list)
    if code_string in code_table:
        return str(code_table[code_string])
    else:
        print('illegal wiring')
        return '0'


lines = open('input.txt', 'r').readlines()
sum_of_numbers = 0
for l in lines:
    signals = l.strip().split(' | ')[0].split(' ')
    output = l.strip().split(' | ')[1].split(' ')
    wiring = decode_wiring(signals + output)
    number = int(''.join([string_to_digit(o, wiring) for o in output]))
    print(number)
    sum_of_numbers += number
print('sum: ', sum_of_numbers)
