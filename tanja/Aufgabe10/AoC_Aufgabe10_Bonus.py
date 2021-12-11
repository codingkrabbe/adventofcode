import sys

# äußere klammer darf nicht zugehen bevor innere klammer zugegangen ist
# fehlende zu sind okay solange äußere nicht zu geht
# äußere die zu früh zugeht ist ein illigal character und muss ausgewiesen werden
from re import match


def main():
    with open('input.txt') as file:
        lines = file.read().splitlines()
        print(len(lines))
        lines = removeIlligalLines(lines)

        scores = []
        for line in lines:
            score = 0
            openBrackets = getOpenBracketsPerLine(line)
            for i in range (len(openBrackets)-1,-1,-1):
                if openBrackets[i] == '[':
                    score = (score * 5) + 2
                if openBrackets[i] == '(':
                    score = (score * 5) + 1

                if openBrackets[i] == '{':
                    score = (score * 5) + 3
                if openBrackets[i] == '<':
                    score = (score * 5) + 4
            scores.append(score)

        scores.sort()
        print(scores[int(len(scores)/2)])


def getOpenBracketsPerLine(line):
    openBrackets = []
    for char in line:
        if char == '[' or char == '(' or char == '{' or char == '<':
            openBrackets.append(char)
        else:
            if char == ']':
                if openBrackets[-1] == '[':
                    openBrackets.pop()
            if char == ')':
                if openBrackets[-1] == '(':
                    openBrackets.pop()
            if char == '}':
                if openBrackets[-1] == '{':
                    openBrackets.pop()
            if char == '>':
                if openBrackets[-1] == '<':
                    openBrackets.pop()
    return openBrackets


def removeIlligalLines(lines):
    illigalChars = []
    newLines = []
    counter = 0
    for line in lines:
        remove = False
        openBrackets = []
        for char in line:
            if char == '[' or char == '(' or char == '{' or char == '<':
                openBrackets.append(char)
            else:
                if char == ']':
                    if openBrackets[-1] == '[':
                        openBrackets.pop()
                    else:
                        illigalChars.append(char)
                        remove = True
                        break
                if char == ')':
                    if openBrackets[-1] == '(':
                        openBrackets.pop()
                    else:
                        illigalChars.append(char)
                        remove = True
                        break
                if char == '}':
                    if openBrackets[-1] == '{':
                        openBrackets.pop()
                    else:
                        illigalChars.append(char)
                        remove = True
                        break
                if char == '>':
                    if openBrackets[-1] == '<':
                        openBrackets.pop()
                    else:
                        illigalChars.append(char)
                        remove = True
                        break
        if not remove:
            newLines.append(line)
    return newLines


if __name__ == '__main__':
    sys.exit(main())
