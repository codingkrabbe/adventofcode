lines = [l.strip() for l in open('input.txt', 'r').readlines()]
char_map = {'{': 1, '}': -1, '(': 2, ')': -2, '[': 3, ']': -3, '<': 4, '>': -4}
char_map_reverse = {1: '{', -1: '}', 2: '(', -2: ')', 3: '[', -3: ']', 4: '<', -4: '>'}
scores = {')': 1, ']': 2, '}': 3, '>': 4}
score_list = []
for l in lines:
    blocks = []
    err = False
    for c in list(l):
        if err:
            continue
        cc = char_map[c]
        if cc > 0:
            blocks.append(cc) # A new block starting)
        else:
            if blocks[-1] == abs(cc): # An old block ends. Let's see, if theres a matching object
                blocks.pop()
            else:
                err = True
    if not err:
        blocks.reverse()
        ending = [char_map_reverse[-1 * n] for n in blocks]
        score = 0
        for ec in ending:
            score = score * 5 + scores[ec]
        score_list.append(score)
score_list.sort()
print(score_list[int((len(score_list) + 1) / 2) - 1])
