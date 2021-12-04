import sys
from collections.__init__ import Counter


def main():
    with open('input.txt') as file:
        linesOxy = [line for line in file]
        linesCO2 = linesOxy.copy()
        for i in range(len(linesOxy[0]) - 1):
            resOxy = dict(Counter(c[i] for c in linesOxy))
            resCO2 = dict(Counter(c[i] for c in linesCO2))

            if len(linesOxy) != 1:
                linesOxy = [x for x in linesOxy if x[i] == '1'] if resOxy['1'] >= resOxy['0'] else [x for x in linesOxy
                                                                                                    if x[i] == '0']
            if len(linesCO2) != 1:
                linesCO2 = [x for x in linesCO2 if x[i] == '0'] if resCO2['1'] >= resCO2['0'] else [x for x in linesCO2
                                                                                                    if x[i] == '1']

    print(int(linesCO2[0].rstrip("\n"), 2) * int(linesOxy[0].rstrip("\n"), 2))

if __name__ == '__main__':
    sys.exit(main())