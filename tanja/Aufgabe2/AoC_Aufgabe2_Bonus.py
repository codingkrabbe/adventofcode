import sys
import re

def main():
    horizontal = 0
    depth = 0
    aim = 0
    with open('input.txt') as file:
        for line in file:
            movement = list(filter(None, re.split('\s', line)))
            if(movement[0] == 'forward'):
                horizontal += int(movement[1])
                depth += aim*int(movement[1])
            if (movement[0] == 'up'): aim -= int(movement[1])
            if (movement[0] == 'down'): aim += int(movement[1])
    print(horizontal*depth)

if __name__ == '__main__':
     sys.exit(main())