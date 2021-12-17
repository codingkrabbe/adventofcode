class Packet:
    def __init__(self, version: int, type_id: int):
        self.version = version
        self.type_id = type_id
        self.sub_packets = []


class LiteralPacket(Packet):
    def __init__(self, version: int, type_id: int, value: int):
        super().__init__(version, type_id)
        self.value = value


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int, length_type_id: int, length: int, sub_packets: list):
        super().__init__(version, type_id)
        self.length_type_id = length_type_id
        self.length = length
        self.sub_packets = sub_packets


def parse(binary_string: str, index: int) -> (int, Packet):
    version = int(binary_string[index: index + 3], 2)
    type_id = int(binary_string[index + 3:index + 6], 2)
    binary_value_string = ''
    if type_id == 4:  # literal packet
        idx = 6
        while binary_string[index + idx] == '1':
            binary_value_string = f'{binary_value_string}{binary_string[index + idx + 1:index + idx + 5]}'
            idx += 5
        binary_value_string = f'{binary_value_string}{binary_string[index + idx + 1:index + idx + 5]}'
        value = int(binary_value_string, 2)
        return index + idx + 5, LiteralPacket(version, type_id, value)
    else:  # operator packet
        length_type_id = int(binary_string[index + 6])
        if length_type_id == 0:  # total length in bits
            length = int(binary_string[index + 7:index + 22], 2)
            sub_packets = []
            index += 22
            starting_index = index
            while index - starting_index < length:
                index, sub_packet = parse(binary_string, index)
                sub_packets.append(sub_packet)
            return index, OperatorPacket(version, type_id, length_type_id, length, sub_packets)
        else:  # number of sub-packets
            length = int(binary_string[index + 7:index + 18], 2)
            sub_packets = []
            index += 18
            while len(sub_packets) < length:
                index, sub_packet = parse(binary_string, index)
                sub_packets.append(sub_packet)
            return index, OperatorPacket(version, type_id, length_type_id, length, sub_packets)


def main():
    hex_bin_mappings = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    lines = open('input.txt', 'r').readlines()
    hex_str = lines[0]
    bin_str = ''
    for char in list(hex_str):
        bin_str = f'{bin_str}{hex_bin_mappings[char]}'
    idx, packet = parse(bin_str, 0)
    version_sum = 0
    packets = [packet]
    while len(packets) > 0:
        curr_packet: Packet = packets.pop()
        packets += curr_packet.sub_packets
        version_sum += curr_packet.version
    print('version sum:', version_sum)


if __name__ == '__main__':
    main()
