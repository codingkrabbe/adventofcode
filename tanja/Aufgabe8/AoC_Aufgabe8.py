import sys


def main():
    counter = 0
    with open('input.txt') as file:
        outputValues = []
        for line in file:
            outputValues.append(line.split('|')[1])

        outputValues = [value.split() for value in outputValues]
        outputValues = flatten(outputValues)
        for value in outputValues:
            if len(value) == 2 or len(value) == 4 or len(value) == 7 or len(value) == 3: counter += 1
        print(outputValues)
        print(counter)


def flatten(list):
    return [item for sublist in list for item in sublist]


if __name__ == '__main__':
    sys.exit(main())
