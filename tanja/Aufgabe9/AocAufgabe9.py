import sys


def main():
    sumRisk = 0
    with open('input.txt') as file:
        heatMap = file.read().splitlines()
        for y in range(len(heatMap)):
            for x in range(len(heatMap[y])):
                if int(heatMap[y][x]) < getUpper(x, y, heatMap) and int(heatMap[y][x]) < getLower(x, y,
                                                                                                  heatMap) and int(
                        heatMap[y][x]) < getLeft(x, y, heatMap) and int(heatMap[y][x]) < getRight(x, y, heatMap):
                    sumRisk += ((int(heatMap[y][x]) + 1))

    print(sumRisk)


def flatten(list):
    return [item for sublist in list for item in sublist]


def getUpper(x, y, heatMap):
    if (y - 1) < 0:
        return 9
    else:
        return int(heatMap[y - 1][x])


def getLower(x, y, heatMap):
    if (y + 1) >= len(heatMap):
        return 9
    else:
        return int(heatMap[y + 1][x])


def getLeft(x, y, heatMap):
    if (x - 1) < 0:
        return 9
    else:
        return int(heatMap[y][x - 1])


def getRight(x, y, heatMap):
    if (x + 1) >= len(heatMap[y]):
        return 9
    else:
        return int(heatMap[y][x + 1])


if __name__ == '__main__':
    sys.exit(main())
