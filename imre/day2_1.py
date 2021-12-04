import pyperclip
input = pyperclip.paste().splitlines()
keys = {'pos': {'f':1, 'u': 0, 'd': 0}, 'depth': {'f':0, 'u': -1, 'd': 1}}
x = y = 0
for i in input:
    val = int(i.split(' ')[1])
    x += val * keys['pos'][i[0]] # horizontal position
    y += val * keys['depth'][i[0]] # depth
print(x,y,x*y)
