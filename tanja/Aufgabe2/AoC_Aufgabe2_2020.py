import sys
import re

def main():
    counter = 0
    with open('input2020.txt') as file:
        for line in file:
            values = list(filter(None, re.split('\s|-|:', line)))
            min = int(values[0])
            max = int(values[1])
            character = values[2]
            value = values[3]
            charCount = value.count(character)
            if (charCount >= min and charCount <= max): counter += 1
    print(counter)

if __name__ == '__main__':
    sys.exit(main())