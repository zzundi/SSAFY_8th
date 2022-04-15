from collections import deque
from copy import deepcopy
t = int(input())
for _ in range(t):
    nums_len = int(input())
    ori_t_cross = 0
    t_num1 = input()
    t_num = t_num1.split('0')
    t_num_len = len(t_num)
    for i in range(t_num_len):
        num = deque(list(map(int, t_num[i].split())))
        num_len = len(num)
        f_cross = 1
        mf_cross = 1
        b_cross = 1
        mb_cross = 1
        fidx, bidx = (0, 0)
        if num_len == 0:
            continue
        while mf_cross == 1 and fidx <= num_len//2-1:
            f_cross = f_cross*num.popleft()
            if f_cross < 0:
                mf_cross = deepcopy(f_cross)
            fidx += 1
        while mb_cross == 1 and bidx <= num_len//2-1:
            b_cross = b_cross*num.pop()
            if b_cross < 0:
                mb_cross = deepcopy(b_cross)
            bidx += 1
        if num_len == 1 and num[0] < 0:
            if '0' in t_num1:
                t_cross = 0
                if t_cross > ori_t_cross:
                    ori_t_cross = t_cross
                continue
        else:
            t_cross = f_cross * b_cross
        if mf_cross == 1 and mb_cross == 1 and num_len % 2 == 1 and num[0] < 0:
            if ori_t_cross < max(f_cross, b_cross):
                ori_t_cross = max(f_cross, b_cross) % 1000000007
        else:
            while len(num) > 0:
                t_cross = t_cross*num.pop()
            if t_cross < 0:
                if mf_cross < mb_cross:
                    if mb_cross == 1:
                        t_cross = t_cross / mf_cross
                    else:
                        t_cross = t_cross / mb_cross
                else:
                    if mf_cross == 1:
                        t_cross = t_cross / mb_cross
                    else:
                        t_cross = t_cross / mf_cross
                if int(t_cross) % 1000000007 > ori_t_cross:
                    ori_t_cross = int(t_cross) % 1000000007
            else:
                    ori_t_cross = int(t_cross) % 1000000007
    print(ori_t_cross)
    