import sys


# äußere klammer darf nicht zugehen bevor innere klammer zugegangen ist
# fehlende zu sind okay solange äußere nicht zu geht
# äußere die zu früh zugeht ist ein illigal character und muss ausgewiesen werden
from re import match


def main():

    illigalChars = []
    with open('input.txt') as file:
        lines = file.read().splitlines()
    for line in lines:
        OpenBrackets = []
        for char in line:
            if char == '[' or char == '(' or char == '{' or char == '<':
                OpenBrackets.append(char)
            else:
                if char == ']':
                    if OpenBrackets[-1] == '[':
                        OpenBrackets.pop()
                    else:
                        illigalChars.append(char)
                        break
                if char == ')':
                    if OpenBrackets[-1] == '(':
                        OpenBrackets.pop()
                    else:
                        illigalChars.append(char)
                        break
                if char == '}':
                    if OpenBrackets[-1] == '{':
                        OpenBrackets.pop()
                    else:
                        illigalChars.append(char)
                        break
                if char == '>':
                    if OpenBrackets[-1] == '<':
                        OpenBrackets.pop()
                    else:
                        illigalChars.append(char)
                        break
    score = 0
    for char in illigalChars:
        if char == ')': score += 3
        if char == ']': score += 57
        if char == '>': score += 25137
        if char == '}': score += 1197

    print(len(illigalChars))
    print(illigalChars)
    print(score)


def flatten(list):
    return [item for sublist in list for item in sublist]


if __name__ == '__main__':
    sys.exit(main())
