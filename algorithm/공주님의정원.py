from collections import defaultdict
import copy
n = int(input())
flowerday = defaultdict(list)
for i in range(n):
    m1, d1, m2, d2 = list(map(int, input().split()))
    if flowerday[m1*100+d1]:
        flowerday[m1*100+d1].append(m2*100 + d2)
    else:
        flowerday[m1*100+d1] = [m2*100 + d2]
f_keys = sorted(list(flowerday.keys()))
max_day, c1, flower_n, idx = (302, 302, 0, 0)
case = 0
while max_day < 1201:
    idx_cnt = 0
    while f_keys[idx] <= c1:
        n_max = max(flowerday[f_keys[idx]])
        if n_max > max_day:
            max_day = n_max
        idx += 1
        idx_cnt += 1
        if idx == len(f_keys):
            print(0)
            case = -2
            break
    if case == -2:
        break
    if idx_cnt == 0 and max_day < 1201 and idx < len(f_keys) - 1:
        idx += 1

    elif idx == len(f_keys):
        if max_day >= 1201:
            flower_n += 1
            break
        else:
            print(0)
            case = -1
            break
    elif idx_cnt == 0 and max_day < 1201:
        print(0)
        case = -1
        break
    else:
        flower_n += 1
        c1 = copy.deepcopy(max_day)



if case > -1:
    print(flower_n)

