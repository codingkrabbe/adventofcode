if __name__ == '__main__':
    depth =0
    horizontal=0
    aim=0
    with open('02-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    for row in text_input:
        if 'forward ' in row:
            horizontal+=int(row.replace('forward ',''))
            depth += int(row.replace('forward ','')) * aim
        if 'up ' in row:
            aim-=int(row.replace('up ',''))
        if 'down ' in row:
            aim+=int(row.replace('down ',''))
    print(horizontal)
    print(depth)
    print(aim)
    print(horizontal*depth)