if __name__ == '__main__':

    with open('01-01-input.txt', 'r', encoding='utf-8') as f:
        result = f.readlines()
    input = {}
    last_depth = 0
    curr_depth = 0
    amount_of_changes = 0
    for idx, i in enumerate(result):
        depth = int(i)
        input.update({idx:depth})

    for idx, j in enumerate(range(len(input))):
        if idx < 3:
            continue
        if input[idx] + input[idx-1] + input[idx-2] > input[idx-1] + input[idx-2] + input[idx-3]:
            amount_of_changes+=1

    print(amount_of_changes)
