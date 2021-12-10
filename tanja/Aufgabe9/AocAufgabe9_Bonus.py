import sys


def main():
    baisins = []
    baisinSizes = []
    with open('input.txt') as file:
        heatMap = file.read().splitlines()
        lowpoints = getLowPoints(heatMap, baisins)

        for point in lowpoints:
            baisinSizes.append(recurse(point[0], point[1], heatMap, []))
        baisinSizes.sort()
        print(baisinSizes[-1] * baisinSizes[-2] * baisinSizes[-3])


def recurse(x, y, heatMap, baisins):
    if not (x, y) in baisins:
        baisins.append((x, y))

    for neighbourCoord in getNeighbourCoordinates(x, y, heatMap):
        if neighbourCoord in baisins:
            continue
        if int(heatMap[neighbourCoord[1]][neighbourCoord[0]]) > int(heatMap[y][x]) and int(
                heatMap[neighbourCoord[1]][neighbourCoord[0]]) < 9:
            recurse(neighbourCoord[0], neighbourCoord[1], heatMap, baisins)

    return len(baisins)


def getLowPoints(heatMap, baisins):
    lowPoints = []
    for y in range(len(heatMap)):
        for x in range(len(heatMap[y])):
            if int(heatMap[y][x]) < getUpper(x, y, heatMap, baisins) and int(heatMap[y][x]) < getLower(x, y, heatMap,
                                                                                                       baisins) and int(
                heatMap[y][x]) < getLeft(x, y, heatMap, baisins) and int(heatMap[y][x]) < getRight(x, y, heatMap,
                                                                                                   baisins):
                lowPoints.append((x, y))
    return lowPoints


def getUpper(x, y, heatMap, baisins):
    if (y - 1) < 0:
        return 9
    elif (x, y - 1) in baisins:
        return 9
    else:
        return int(heatMap[y - 1][x])


def getLower(x, y, heatMap, baisins):
    if (y + 1) >= len(heatMap):
        return 9
    elif (x, y + 1) in baisins:
        return 9
    else:
        return int(heatMap[y + 1][x])


def getLeft(x, y, heatMap, baisins):
    if (x - 1) < 0:
        return 9
    elif (x - 1, y) in baisins:
        return 9
    else:
        return int(heatMap[y][x - 1])


def getRight(x, y, heatMap, baisins):
    if (x + 1) >= len(heatMap[y]):
        return 9
    elif (x + 1, y) in baisins:
        return 9
    else:
        return int(heatMap[y][x + 1])


def getNeighbours(x, y, heatMap, baisins):
    neighbours = []
    neighbours.append(getUpper(x, y, heatMap, baisins))
    neighbours.append(getLower(x, y, heatMap, baisins))
    neighbours.append(getLeft(x, y, heatMap, baisins))
    neighbours.append(getRight(x, y, heatMap, baisins))
    return neighbours


def getUpperCoordinates(x, y, heatMap):
    if (y - 1) < 0:
        return False
    else:
        return x, y - 1


def getLowerCoordinates(x, y, heatMap):
    if (y + 1) >= len(heatMap):
        return False
    else:
        return x, y + 1


def getLeftCoordinates(x, y, heatMap):
    if (x - 1) < 0:
        return False
    else:
        return x - 1, y


def getRightCoordinates(x, y, heatMap):
    if (x + 1) >= len(heatMap[y]):
        return False
    else:
        return x + 1, y


def getNeighbourCoordinates(x, y, heatMap):
    coordinates = []
    if getUpperCoordinates(x, y, heatMap): coordinates.append(getUpperCoordinates(x, y, heatMap))
    if getLowerCoordinates(x, y, heatMap): coordinates.append(getLowerCoordinates(x, y, heatMap))
    if getLeftCoordinates(x, y, heatMap): coordinates.append(getLeftCoordinates(x, y, heatMap))
    if getRightCoordinates(x, y, heatMap): coordinates.append(getRightCoordinates(x, y, heatMap))
    return coordinates


if __name__ == '__main__':
    sys.exit(main())
