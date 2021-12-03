import pyperclip
input = pyperclip.paste().splitlines()
db = {'oxy':0, 'co2':0} # Keep track of results

def convert_to_decimal(bin_str: str):
    return sum([int(n) * pow(2, len(bin_str) - j - 1) for j, n in enumerate(bin_str)])

for x in db.keys():
    bit_pos = 0
    remaining_inputs = input.copy()
    while len(remaining_inputs) > 1:
        ones = sum([int(i[bit_pos]) for i in remaining_inputs]) # num of ones in current position        
        val = int(ones >= len(remaining_inputs) / 2) * int(x == 'oxy') + \
              int(ones <  len(remaining_inputs) / 2) * int(x == 'co2')
        remaining_inputs = [i for i in remaining_inputs if int(i[bit_pos]) == val]
        bit_pos += 1
    db[x] = convert_to_decimal(remaining_inputs[0])
print(db['oxy'],db['co2'],db['oxy']*db['co2'])
