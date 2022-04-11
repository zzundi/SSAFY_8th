from collections import deque


n = int(input())

for i in range(n):
    t_cost = 0
    chapter = int(input())
    cost = list(map(int, input().split()))
    while True:
        cat1 = min(cost)
        cat2 = cost.pop(0)
        t_cost += cat1 + cat2
        cost.append(cat1+cat2)
        cost.sort()
        if len(cost) < 2:
            break
    print(t_cost)
