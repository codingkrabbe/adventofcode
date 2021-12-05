import sys
import re


def main():
    with open('input.txt') as file:
        counter = 0
        winningNumbers = file.readline().rstrip("\n").split(',')
        lines = file.read().splitlines()
        bingoList = []
        bingoBoards = []
        for line in lines:
            if (line == '' or line == '\n'):
                continue
            if line[0] == ' ': line = line[1:]
            bingoList.append(re.split('\s+', line))
        bingoBoardX = len(bingoList[0])
        bingoBoards.append(bingoList[0])

        for i in range(1, len(bingoList)):
            # print(len(bingoList[i]))
            counter += 1
            if (counter == bingoBoardX):
                counter = 0
                bingoBoards.append(bingoList[i].copy())
            else:
                bingoBoards[int(i / bingoBoardX)] += bingoList[i].copy()

        for i in range(len(bingoBoards)):
            bingoBoards[i] = [(number, False) for number in bingoBoards[i]]

        lastBINGO = False
        WinningBoards = []
        for winningNumber in winningNumbers:
            for i in range(len(bingoBoards)):
                bingoBoards[i] = [(t[0], True) if t[0] == winningNumber else (t[0], t[1]) for t in bingoBoards[i]]
                counterTrueRows = 0
                counterTrueColumns = 0

                if not (i in WinningBoards):
                    counter = 0
                    for j in range(len(bingoBoards[i])):
                        if counter < bingoBoardX:
                            counter += 1

                        # columnwin
                        if bingoBoards[i][j % bingoBoardX * bingoBoardX + int(j / bingoBoardX)][1] == True:
                            counterTrueColumns += 1
                        if (counterTrueColumns == bingoBoardX):
                            WinningBoards.append(i)
                            print('column' + ' ' + 'board' + str(i))
                            if len(WinningBoards) == len(bingoBoards):
                                lastBINGO = True
                            break

                        # rownwin
                        if bingoBoards[i][j][1] == True:
                            counterTrueRows += 1
                        if (counterTrueRows == bingoBoardX):
                            WinningBoards.append(i)
                            print('row' + ' ' + 'board' + str(i))
                            if len(WinningBoards) == len(bingoBoards):
                                lastBINGO = True
                            break

                        if counter >= bingoBoardX:
                            counter = 0
                            counterTrueRows = 0
                            counterTrueColumns = 0


                if lastBINGO == True:
                    value = sum(int(t[0]) for t in bingoBoards[i] if t[1] != True)
                    print('value' + str(value))
                    print('winningnumber' + str(winningNumber))
                    print('winningboard' + str(i))
                    print(value * int(winningNumber))
                    print('winningboards' + str(WinningBoards))
                    print('winningnumbers' + str(winningNumbers))
                    return


if __name__ == '__main__':
    sys.exit(main())
