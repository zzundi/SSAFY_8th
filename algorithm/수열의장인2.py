from collections import deque
from copy import deepcopy
t = int(input())
for _ in range(t):
    nums_len = int(input())
    nums_left = deque(map(int, input().split()))
    nums_right = deepcopy(nums_left)
    num_minus = 0
    two_cnt = 0
    for _ in range(nums_len):
        num = nums_left.popleft()
        if num < 0:
            num_minus += 1
        elif num == 0:
            num_minus == 0
            continue
        if num_minus % 2 == 0:
            if num == 2 or num == -2:
                two_cnt += 1
        if two_cnt
        

