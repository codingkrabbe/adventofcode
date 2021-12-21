from math import isclose
import numpy as np
from scipy.spatial.transform.rotation import Rotation
from scipy.spatial.distance import cityblock

MIN_OVERLAPPING_BEACONS = 12


scanner_positions = []


class Beacon:
    def __init__(self, x: int, y: int, z: int):
        self.pos = np.array([x, y, z])


class Scanner:
    def __init__(self, index: int):
        self.index = index
        self.beacons = None
        self.differences = None

    def set_beacons(self, beacons: list[Beacon]):
        self.beacons = beacons
        self.differences: list[list[float]] = []
        for i in range(len(beacons)):
            row = []
            for j in range(i):
                difference = np.linalg.norm(np.array(beacons[i].pos) - np.array(beacons[j].pos))
                row.append(difference)
            self.differences.append(row)


def get_max_overlaps(scanner1: Scanner, scanner2: Scanner):
    num_matching_differences = 0
    indices_1 = set()
    indices_2 = set()
    for i1 in range(len(scanner1.beacons)):  # check if there are at least 12 euclidean distance matches
        for j1 in range(i1):
            for i2 in range(len(scanner2.beacons)):
                for j2 in range(i2):
                    if isclose(scanner1.differences[i1][j1], scanner2.differences[i2][j2]):
                        indices_1.add(i1)
                        indices_1.add(j1)
                        indices_2.add(i2)
                        indices_2.add(j2)
                        num_matching_differences += 1
    return num_matching_differences, indices_1, indices_2


def is_close(one: list[float], other: list[float]):
    value = True
    for i in range(len(one)):
        if not isclose(one[i], other[i]):
            value = False
    return value


def get_possible_beacon_rotations(beacons: list[Beacon]):
    rotations = []
    for x_degrees in range(0, 360, 90):
        for y_degrees in range(0, 360, 90):
            for z_degrees in range(0, 360, 90):
                rotation = []
                for beacon in beacons:
                    rotation.append(rotate_point(beacon.pos, x_degrees, y_degrees, z_degrees))
                rotations.append(rotation)
    return rotations


def rotate_point(point: np.array, x_degrees: int, y_degrees: int, z_degrees: int):
    x_radians = np.radians(x_degrees)
    rotation_axis = np.array([1, 0, 0])
    rotation_vector = x_radians * rotation_axis
    rotation = Rotation.from_rotvec(rotation_vector)
    rotated_point = rotation.apply(point)

    y_radians = np.radians(y_degrees)
    rotation_axis = np.array([0, 1, 0])
    rotation_vector = y_radians * rotation_axis
    rotation = Rotation.from_rotvec(rotation_vector)
    rotated_point = rotation.apply(rotated_point)

    z_radians = np.radians(z_degrees)
    rotation_axis = np.array([0, 0, 1])
    rotation_vector = z_radians * rotation_axis
    rotation = Rotation.from_rotvec(rotation_vector)
    rotated_point = rotation.apply(rotated_point)

    return np.array(rotated_point)


def get_position_pair(positions_1, positions_2, diff):
    for position_1 in positions_1:
        for position_2 in positions_2:
            if isclose(np.linalg.norm(position_1 - position_2), diff):
                return position_1, position_2


def get_new_beacon_positions(unified_scanner, indices_1, new_scanner):
    global scanner_positions
    relevant_unified_beacons = \
        [beacon for idx, beacon in enumerate(unified_scanner.beacons) if idx in indices_1]
    possible_rotations = get_possible_beacon_rotations(new_scanner.beacons)
    for possible_rotation in possible_rotations:
        diffs = {}
        for relevant_unified_beacon in relevant_unified_beacons:
            for beacon_pos in possible_rotation:
                diff = np.linalg.norm(relevant_unified_beacon.pos - beacon_pos)
                key_found = False
                for key in diffs.keys():
                    if isclose(diff, key):
                        diffs[key] += 1
                        key_found = True
                if not key_found:
                    diffs[diff] = 1
        for diff in diffs.keys():
            matching_diff_found = False
            if not matching_diff_found and diffs[diff] >= 12:
                matching_diff_found = True
                unified_positions = [beacon.pos for beacon in relevant_unified_beacons]
                position_pair = get_position_pair(unified_positions, possible_rotation, diff)
                translation_vector = position_pair[0] - position_pair[1]
                scanner_positions.append(np.array([translation_vector]))
                for i in range(len(possible_rotation)):
                    possible_rotation[i] = possible_rotation[i] + translation_vector
                new_beacon_positions = []
                for beacon_pos in possible_rotation:
                    already_exists = False
                    for relevant_unified_beacon in relevant_unified_beacons:
                        if is_close(beacon_pos, relevant_unified_beacon.pos):
                            already_exists = True
                    if not already_exists:
                        new_beacon_positions.append(beacon_pos)
                return new_beacon_positions


def main():
    global scanner_positions
    lines = open('input.txt', 'r').readlines()
    scanners = []
    scanner = None
    beacons = []
    same_distance_threshold = (MIN_OVERLAPPING_BEACONS * (MIN_OVERLAPPING_BEACONS - 1)) / 2
    for line in lines:
        if 'scanner' in line:
            index = int(line.strip()[len('--- scanner '):-len(' ---')])
            if scanner is not None:
                scanner.set_beacons(beacons)
                scanners.append(scanner)
            scanner = Scanner(index)
            beacons = []
        else:
            comma_split = line.strip().split(',')
            if len(comma_split) == 3:
                x = int(comma_split[0])
                y = int(comma_split[1])
                z = int(comma_split[2])
                beacon = Beacon(x, y, z)
                beacons.append(beacon)
    scanner.set_beacons(beacons)
    scanners.append(scanner)
    unified_scanner = scanners[0]
    scanner_positions.append(np.array([0, 0, 0]))
    scanners.remove(scanners[0])
    while len(scanners) > 0:
        print(f'{len(scanners)} scanners yet to be unified')
        step_completed = False
        for j in range(len(scanners)):
            if j < len(scanners):
                if not step_completed:
                    num_overlapping_beacons, indices_1, indices_2 = get_max_overlaps(unified_scanner, scanners[j])
                    if num_overlapping_beacons >= same_distance_threshold / 2:
                        new_beacon_positions = get_new_beacon_positions(unified_scanner, indices_1, scanners[j])
                        if new_beacon_positions is not None:
                            unified_beacons = unified_scanner.beacons
                            for pos in new_beacon_positions:
                                unified_beacons.append(Beacon(pos[0], pos[1], pos[2]))
                            unified_scanner.set_beacons(unified_beacons)
                            scanners.remove(scanners[j])
                            step_completed = True
                            print(f'Unified scanner and scanner at index {j} overlap - added to unified map')
    max_distance = 0
    for i in range(len(scanner_positions)):
        for j in range(len(scanner_positions)):
            distance = cityblock(scanner_positions[i], scanner_positions[j])
            if distance > max_distance:
                max_distance = distance
    print('Max distance between scanners:', round(max_distance))


if __name__ == '__main__':
    main()
