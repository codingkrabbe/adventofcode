import sys


def main():
    lines = open('input.txt', 'r').readlines()
    positions = list(map(int, lines[0].split(',')))
    min_position = min(positions)
    max_position = max(positions)
    min_fuel_cost = sys.maxsize * 2 + 1
    for i in range(min_position, max_position + 1):
        fuel_cost = 0
        for position in positions:
            fuel_cost += abs(position - i)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    print('Minimum fuel cost to align: ' + str(min_fuel_cost))


if __name__ == '__main__':
    main()
