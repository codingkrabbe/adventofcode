import pyperclip
input = pyperclip.paste().splitlines()
keys = {'aim': {'f':0, 'u': -1, 'd': 1}, 'pos': {'f':1, 'u': 0, 'd': 0}}
a = x = y = 0
for i in input:
    val = int(i.split(' ')[1])
    a += val * keys['aim'][i[0]] # aim
    x += val * keys['pos'][i[0]] # position
    y += val * a * keys['pos'][i[0]] # depth
print(x, y, x * y)
