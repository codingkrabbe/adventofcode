lines = [l.strip() for l in open('input.txt', 'r').readlines()]
char_map = {'{': 1, '}': -1, '(': 2, ')': -2, '[': 3, ']': -3, '<': 4, '>': -4}
char_map_reverse = {1: '{', -1: '}', 2: '(', -2: ')', 3: '[', -3: ']', 4: '<', -4: '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
score = 0
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
                # print(l + ' - Syntax error. Expected: ' + char_map_reverse[-1 * blocks[-1]] + ' got: ' + c)
                score += scores[c]
                err = True
print(score)
