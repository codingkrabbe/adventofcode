import math
import copy
lines = open('input.txt', 'r').readlines()
nums = []
for l in lines:
    nums.append(eval(l.strip()))


def find_first_number_depth(l: list):
    d = 1
    for i in range(len(l)):
        if type(l[i]) == int:
            return i
        else:
            d += find_first_number_depth(l[i])
            return d


def add_to_last_number(l: list, val:int):
    for i in range(len(l) -1, -1, -1):
        if type(l[i]) == int:
            l[i] += val
            return l
        else:
            return add_to_last_number(l[i], val)


def add_to_first_number(l:list, depth: int, val: int):
    if depth == 0:
        l[0] += val
    if depth == 1:
        l[0][0] += val
    if depth == 2:
        l[0][0][0] += val
    if depth == 3:
        l[0][0][0][0] += val
    if depth == 4:
        l[0][0][0][0][0] += val
    if depth == 5:
        l[0][0][0][0][0][0] += val
    if depth == 6:
        l[0][0][0][0][0][0][0] += val
    if depth == 7:
        l[0][0][0][0][0][0][0][0] += val
    if depth == 8:
        l[0][0][0][0][0][0][0][0][0] += val
    if depth == 9:
        l[0][0][0][0][0][0][0][0][0][0] += val
    if depth == 10:
        l[0][0][0][0][0][0][0][0][0][0][0] += val
    return l

def explode(listt):
    li = copy.deepcopy(listt)
    explode = False
    for a in range(len(li)):
        aa = li[a]
        if type(aa) != list: continue
        for b in range(len(aa)):
            bb = li[a][b]
            if type(bb) != list: continue
            for c in range(len(bb)):
                cc = li[a][b][c]
                if type(cc) != list: continue
                for d in range(len(cc)):
                    dd = li[a][b][c][d]
                    if type(dd) != list: continue
                    # This is a eligable nested number.
                    explode = True
                    break
                if explode: break
            if explode: break
        if explode: break
    if not explode: return li
    # Find left number
    found_number = False
    if d > 0:
        for i in range(d - 1, -1, -1):
            if type(li[a][b][c][i]) == int:
                li[a][b][c][i] += li[a][b][c][d][0]
            else:
                add_to_last_number(li[a][b][c][i], li[a][b][c][d][0])
            found_number = True
            break
    if not found_number and c > 0:
        for i in range(c - 1, -1, -1):
            if type(li[a][b][i]) == int:
                li[a][b][i] += li[a][b][c][d][0]
            else:
                add_to_last_number(li[a][b][i], li[a][b][c][d][0])
            found_number = True
            break
    if not found_number and b > 0:
        for i in range(b - 1, -1, -1):
            if type(li[a][i]) == int:
                li[a][i] += li[a][b][c][d][0]
            else:
                add_to_last_number(li[a][i], li[a][b][c][d][0])
            found_number = True
            break
    if not found_number and a > 0:
        for i in range(a - 1, -1, -1):
            if type(li[i]) == int:
                li[i] += li[a][b][c][d][0]
            else:
                add_to_last_number(li[i], li[a][b][c][d][0])
            break
    # Find right number
    found_number = False
    if len(cc) - 1 > d:
        for i in range(d + 1, len(cc)):
                found_number = True
                if type(li[a][b][c][i]) == int:
                    li[a][b][c][i] += li[a][b][c][d][1]
                else:
                    li[a][b][c][i] = add_to_first_number(li[a][b][c][i],
                                                            find_first_number_depth(li[a][b][c][i]),
                                                            li[a][b][c][d][1])
                break
    if not found_number and len(bb) - 1 > c:
        for i in range(c + 1, len(bb)):
                found_number = True
                if type(li[a][b][i]) == int:
                    li[a][b][i] += li[a][b][c][d][1]
                else:
                    li[a][b][i] = add_to_first_number(li[a][b][i],
                                                            find_first_number_depth(li[a][b][i]),
                                                            li[a][b][c][d][1])
                break
    if not found_number and len(aa) - 1 > b:
        for i in range(b + 1, len(aa)):
            found_number = True
            if type(li[a][i]) == int:
                li[a][i] += li[a][b][c][d][1]
            else:
                li[a][i] = add_to_first_number(li[a][i], find_first_number_depth(li[a][i]),
                                                     li[a][b][c][d][1])
            break
    if not found_number and len(li) - 1 > a:
        for i in range(a + 1, len(li)):
            found_number = True
            if type(li[i]) == int:
                li[i] += li[a][b][c][d][1]
            else:
                li[i] = add_to_first_number(li[i], find_first_number_depth(li[i]),
                                                  li[a][b][c][d][1])
            break
    li[a][b][c][d] = 0
    return li


def split(n: int):
    return [int(math.trunc(n/2)), int(math.ceil(n/2))]


def split_first(listt: list):
    li = copy.deepcopy(listt)
    found_it = False
    for i in range(len(li)):
        if type(li[i]) == int:
            if li[i] > 9:
                li[i] = split(li[i])
                return li, True
        else:
            li[i], found_it = split_first(li[i])
            if found_it:
                return li, found_it
    return li, found_it


def reduce_sailfishnum(sf):
    while True:
        if sf != explode(copy.deepcopy(sf)):
            sf = explode(copy.deepcopy(sf))
        elif sf != split_first(copy.deepcopy(sf))[0]:
            sf  = split_first(copy.deepcopy(sf))[0]
        else:
            break
    return sf


num = copy.deepcopy(nums[0])
for n in nums[1:]:
    num = [copy.deepcopy(num) , n]
    num = reduce_sailfishnum(copy.deepcopy(num))
print(num)


def magnitude(num):
    if type(num[0]) == int:
        left = num[0]
    else:
        left = magnitude(num[0])
    if type(num[1]) == int:
        right = num[1]
    else:
        right = magnitude(num[1])
    return 3 * left + 2 * right


print(magnitude(num))