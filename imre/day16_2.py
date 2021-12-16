to_binstr = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
file_content = open('input_d16.txt', 'r').readline().strip()
data_string = ''.join([to_binstr[c] for c in list(file_content)])


def next_please(bits):
    if len(bits) < 6:
        return {}, ''
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    if type_id == 4:
        # Literal value
        bits = bits[6:]
        number = ''
        continue_reading = True
        while continue_reading:
            continue_reading = bits[0] == '1'
            number += bits[1:5]
            bits = bits[5:]
        data = int(number, 2)
    else:
        # Operator
        subpackets = []
        if bits[6] == '0':
            bits = bits[7:]
            subpackets_bit_length = int(bits[:15], 2)
            bits = bits[15:]
            subpacket_data = bits[:subpackets_bit_length]
            continue_reading = True
            while continue_reading:
                p, subpacket_data = next_please(subpacket_data)
                if p:
                    subpackets.append(p)
                else:
                    continue_reading = False
            bits = bits[subpackets_bit_length:]
            data = subpackets
        else:
            bits = bits[7:]
            num_of_subpackets = int(bits[:11], 2)
            bits = bits[11:]
            for i in range(num_of_subpackets):
                p, bits = next_please(bits)
                subpackets.append(p)
            data = subpackets
    return {'v': version, 't': type_id, 'data': data}, bits


def evaluate_packet(p):
    value = 0
    if p['t'] == 0: value = sum([evaluate_packet(sp) for sp in p['data']]) # sum
    if p['t'] == 2: value = min([evaluate_packet(sp) for sp in p['data']]) # minimum
    if p['t'] == 3: value = max([evaluate_packet(sp) for sp in p['data']]) # maximum
    if p['t'] == 4: value = p['data'] # literal value
    if p['t'] == 5: value = int(evaluate_packet(p['data'][0]) > evaluate_packet(p['data'][1])) # greater than
    if p['t'] == 6: value = int(evaluate_packet(p['data'][0]) < evaluate_packet(p['data'][1])) # less than
    if p['t'] == 7: value = int(evaluate_packet(p['data'][0]) == evaluate_packet(p['data'][1])) # equal
    if p['t'] == 1:
        # product
        value = 1
        for sp in p['data']:
            value *= evaluate_packet(sp)
    return value


packet, rest = next_please(data_string)
print(evaluate_packet(packet))
