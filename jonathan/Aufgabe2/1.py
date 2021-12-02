forward, depth = 0, 0
lines = open('input.txt', 'r').readlines()
for line in lines:
    command = line.split(' ')
    if command[0] == 'forward':
        forward += int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    else:
        depth -= int(command[1])
print(depth * forward)
