if __name__ == '__main__':

    with open('01-input.txt', 'r', encoding='utf-8') as f:
        result = f.readlines()
    input = []
    last_depth = 0
    curr_depth = 0
    amount_of_changes = 0
    for idx, i in enumerate(result):
        depth = int(i)
        input.append(depth)
        curr_depth = depth
        if idx > 0:
            if curr_depth > last_depth:
                amount_of_changes +=1
        last_depth = depth
    print(amount_of_changes)
