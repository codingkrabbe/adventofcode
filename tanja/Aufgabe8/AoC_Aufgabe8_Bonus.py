import sys


def main():
    sum = 0
    with open('input.txt') as file:

        for line in file:
            # fill dict
            splitLine = line.split('|')
            splitLine = [signal.split() for signal in splitLine]
            outputValues = splitLine[1]
            inputSignals = splitLine[0]
            dictNumbers = get1478(dict(), inputSignals)
            dictNumbers = get396(dictNumbers, inputSignals)
            dictNumbers = get520(dictNumbers, inputSignals)

            # sumValues
            strValue = ''
            for value in outputValues:
                for numberValue in dictNumbers.values():
                    if hasSameChars(value, numberValue):
                        strValue += str(list(dictNumbers.keys())[list(dictNumbers.values()).index(numberValue)])

            sum += int(strValue)
        print('sum = ' + str(sum))


def flatten(list):
    return [item for sublist in list for item in sublist]


def isSignal3(signal, dict):
    if sorted(common(dict[7], signal)) == sorted(dict[7]):
        if (len(signal) == len(dict[7]) + 2):
            return True
    return False


def isSignal9(signal, dict):
    if sorted(common(dict[4], signal)) == sorted(dict[4]):
        if (len(signal) == len(dict[4]) + 2):
            return True
    return False


def isSignal6(signal, dict):
    dist48 = dist(dict[4], dict[8])
    dist41 = dist(dict[1], dict[4])
    almost6 = dist41 + dist48
    if sorted(common(almost6, signal)) == sorted(almost6):
        if (len(signal) == len(almost6) + 1):
            return True
    return False


def isSignal5or2or0(signal, dict):
    if (len(signal) == len(dict[6]) - 1):
        if sorted(common(dict[6], signal)) == sorted(signal):
            return 5
        else:
            return 2
    return 0


def hasSameChars(str1, str2):
    return sorted(str1) == sorted(str2)


def dist(shorter, longer):
    dist = ''
    for c in longer:
        if c not in shorter:
            dist = dist + c
    return dist


def common(shorter, longer):
    common = ''
    for c in longer:
        if c in shorter:
            common = common + c
    return common


def get1478(dictNumbers, inputSignals):
    for value in inputSignals:
        if len(value) == 2: dictNumbers[1] = value
        if len(value) == 4: dictNumbers[4] = value
        if len(value) == 3: dictNumbers[7] = value
        if len(value) == 7: dictNumbers[8] = value
    return dictNumbers


def get396(dictNumbers, inputSignals):
    for signal in inputSignals:
        if signal not in dictNumbers.values():
            if isSignal3(signal, dictNumbers): dictNumbers[3] = signal
            if isSignal9(signal, dictNumbers): dictNumbers[9] = signal
            if isSignal6(signal, dictNumbers): dictNumbers[6] = signal;
    return dictNumbers


def get520(dictNumbers, inputSignals):
    for signal in inputSignals:
        if signal not in dictNumbers.values():
            dictNumbers[isSignal5or2or0(signal, dictNumbers)] = signal
    return dictNumbers


if __name__ == '__main__':
    sys.exit(main())
