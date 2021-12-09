lines = open('input.txt', 'r').readlines()
count = 0
for l in lines:
    count += len([word for word in l.strip().split(' | ')[1].split(' ') if len(word) in [2, 3, 4, 7]])
print(count)