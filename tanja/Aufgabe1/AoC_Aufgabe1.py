lastLine = 0
counter = 0
with open("input.txt") as f:
    lastLine = int(f.readline().rstrip())
with open('input.txt') as file:
    for line in file:
        if(lastLine < int(line)):
            counter += 1
        lastLine= int(line)
print(counter)