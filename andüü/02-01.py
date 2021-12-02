if __name__ == '__main__':
    depth =0
    horizontal=0
    with open('02-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    for row in text_input:
        if 'forward ' in row:
            horizontal+=int(row.replace('forward ',''))
        if 'up ' in row:
            depth-=int(row.replace('up ',''))
        if 'down ' in row:
            depth+=int(row.replace('down ',''))
    print(horizontal)
    print(depth)
    print(horizontal*depth)