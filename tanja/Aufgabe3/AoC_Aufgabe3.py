import sys
from collections.__init__ import Counter

def main():
    gamma = ''
    epsilon = ''
    with open('input.txt') as file:
        lines = [line for line in file]
        for i in range(len(lines[0])-1):
            res = dict(Counter(c[i] for c in lines))
            if res['1'] > res['0']:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
    print(int(gamma,2)*int(epsilon,2))

if __name__ == '__main__':
     sys.exit(main())