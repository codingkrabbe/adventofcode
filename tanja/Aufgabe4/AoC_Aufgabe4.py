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

        # print(bingoBoards)
        print(bingoList)
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

        BINGO = False
        for winningNumber in winningNumbers:
            for i in range(len(bingoBoards)):
                bingoBoards[i] = [(t[0], True) if t[0] == winningNumber else (t[0], t[1]) for t in bingoBoards[i]]
                counterTrueRows = 0
                counterTrueColumns = 0


                counter = 0
                for j in range(len(bingoBoards[i])):
                    if counter < bingoBoardX:
                        counter += 1
                    #rownwin
                    if bingoBoards[i][j][1] == True:
                        counterTrueRows += 1
                    if (counterTrueRows == bingoBoardX):
                        print("woheeRow")
                        print(bingoBoards[i])
                        print(j)
                        BINGO = True
                        break

                    #columnwin
                    if bingoBoards[i][j % bingoBoardX * bingoBoardX + int(j / 5)][1] == True:
                        counterTrueColumns += 1
                    if (counterTrueColumns == bingoBoardX):
                        print("woheeColumn")
                        print(bingoBoards[i])
                        BINGO = True
                        break

                    if counter >= bingoBoardX:
                        counter = 0
                        counterTrueRows = 0
                        counterTrueColumns = 0

                if BINGO == True:
                    value = sum(int(t[0]) for t in bingoBoards[i] if t[1] != True)
                    print(value)
                    print(winningNumber)
                    print(i)
                    print(len(bingoBoards))
                    print(value * int(winningNumber))
                    print(bingoBoards[45])
                    return


if __name__ == '__main__':
    sys.exit(main())
