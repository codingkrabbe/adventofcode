import sys

lastValue = sys.maxsize
linesAdd = 0
counter = 0
i = 0

with open('input.txt') as file:
    lines = [line for line in file]
    for line in lines:
        i += 1
        linesAdd += int(line)
        if(i >= 3):
            if (lastValue < linesAdd):
                counter += 1
            lastValue = linesAdd
            linesAdd -= int(lines[i-3])
print(counter)