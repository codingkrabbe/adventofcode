import sys

counter = 0
def main():

    with open('input.txt') as file:
        global counter
        octopuses = file.read().splitlines()
        octopuses = [list(map(int, line)) for line in octopuses]
        print(octopuses)
        for i in range(100):
            #stepflashes
            for y in range(len(octopuses)):
                for x in range(len(octopuses[y])):
                    octopuses[y][x] += 1
                    if octopuses[y][x] == 10:
                        flash(x,y,octopuses)
            #resetflashies
            for y in range(len(octopuses)):
                for x in range(len(octopuses[y])):
                    if octopuses[y][x] >= 10:
                        octopuses[y][x] = 0


        print(counter)



def flash(x,y,octopuses):
    global counter
    counter += 1
    for neighbourCoord in getNeighbourCoordinates(x,y,octopuses):
        nX = neighbourCoord[0]
        nY = neighbourCoord[1]
        octopuses[nY][nX] += 1
        if octopuses[nY][nX] == 10:
            flash(nX,nY,octopuses)
    return
def getUpperCoordinates(x, y, octopuses):
    if (y - 1) < 0:
        return False
    else:
        return x, y - 1


def getLowerCoordinates(x, y, octopuses):
    if (y + 1) >= len(octopuses):
        return False
    else:
        return x, y + 1


def getLeftCoordinates(x, y, octopuses):
    if (x - 1) < 0:
        return False
    else:
        return x - 1, y


def getRightCoordinates(x, y, octopuses):
    if (x + 1) >= len(octopuses[y]):
        return False
    else:
        return x + 1, y


def getUpperRightCoordinates(x, y, octopuses):
    if (x + 1) >= len(octopuses[y]):
        return False
    elif (y - 1) < 0:
        return False
    else:
        return x + 1, y - 1


def getUpperLeftCoordinates(x, y, octopuses):
    if (x - 1) < 0:
        return False
    elif (y - 1) < 0:
        return False
    else:
        return x - 1, y - 1


def getLowerRightCoordinates(x, y, octopuses):
    if (y + 1) >= len(octopuses):
        return False
    if (x + 1) >= len(octopuses[y]):
        return False
    else:
        return x + 1, y + 1


def getLowerLeftCoordinates(x, y, octopuses):
    if (y + 1) >= len(octopuses):
        return False
    if (x - 1) < 0:
        return False
    else:
        return x - 1, y + 1


def getNeighbourCoordinates(x, y, octopuses):
    coordinates = []
    if getUpperCoordinates(x, y, octopuses): coordinates.append(getUpperCoordinates(x, y, octopuses))
    if getLowerCoordinates(x, y, octopuses): coordinates.append(getLowerCoordinates(x, y, octopuses))
    if getLeftCoordinates(x, y, octopuses): coordinates.append(getLeftCoordinates(x, y, octopuses))
    if getRightCoordinates(x, y, octopuses): coordinates.append(getRightCoordinates(x, y, octopuses))
    # maybe test this:
    if getUpperRightCoordinates(x, y, octopuses): coordinates.append(getUpperRightCoordinates(x, y, octopuses))
    if getUpperLeftCoordinates(x, y, octopuses): coordinates.append(getUpperLeftCoordinates(x, y, octopuses))
    if getLowerRightCoordinates(x, y, octopuses): coordinates.append(getLowerRightCoordinates(x, y, octopuses))
    if getLowerLeftCoordinates(x, y, octopuses): coordinates.append(getLowerLeftCoordinates(x, y, octopuses))
    return coordinates


if __name__ == '__main__':
    sys.exit(main())
