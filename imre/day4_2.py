import re
lines = open('input.txt', 'r').readlines()
bingo_list = [int(n) for n in lines[0].split(',')] # list of numbers drawn in bingo
cards = dict()
winning_cards = set()
for i in range(int((len(lines)-1) / 6)):
    cards[i] = [list(map(int, re.split(r'\s+', l.strip()))) for l in lines[2 + 6 * i:2 + 6 * i + 5]] # dict of cards
for b in range(len(bingo_list)):
    for c in cards.keys():
        cols = [[cards[c][j][i] for j in range(len(cards[c]))] for i in range(len(cards[c][0])-1, -1, -1)]
        for row in cards[c] + cols: # list of all lines and columns in the card
            if len([l for l in row if l not in bingo_list[:b + 1]]) < 1: # If all numbers bingo'd in row or column
                winning_cards.add(c)
                if len(winning_cards) == len(cards): # The last card has just been added. Time to stop.
                    card_val = sum([n for n in
                                    [element for sub in cards[c] for element in sub]
                                    if n not in bingo_list[:b + 1]])  # Sum of all non bingo'd elements on card
                    print(card_val, bingo_list[b], card_val * bingo_list[b])
                    exit()
