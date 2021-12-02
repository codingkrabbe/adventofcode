import sys
import re

def main():
    counter = 0
    with open('input2020.txt') as file:
        for line in file:
            values = list(filter(None, re.split('\s|-|:', line)))
            pos1 = int(values[0])
            pos2 = int(values[1])
            character = values[2]
            value = values[3]
            if (value[pos1-1] == character and value[pos2-1] != character or value[pos1-1] != character and value[pos2-1] == character): counter += 1
    print(counter)

if __name__ == '__main__':
    sys.exit(main())