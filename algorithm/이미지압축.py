from collections import defaultdict
from email.policy import default
from math import log2


n, m = map(int, input().split())
i = 1
while True:
    if n > m:
        if n <= 2 ** i:
            need_n = 2**i - n
            need_m = 2**i - m
            break
        else:
            i += 1
    else:
        if m <= 2 ** i:
            need_m = 2**i - m
            need_n = 2**i - n
            break
        else:
            i += 1

map = [[0]*(m+need_m) for _ in range(n+need_n)]

for i in range(n):
    input_num = input()
    for j in range(m):
        map[i][j] = int(input_num[j])
new_map = []
for i in map:
    new_map += i
map_len = len(map)
node_stage = int(log2(map_len)) + 1
comp_map = defaultdict(list)

for i in range(node_stage):
    div = [(i, j, k) for j in range(2**i) for k in range(2**i)]
    for d in div:
        if d == (0, 0, 0):
            for j in range(map_len):
                for k in range(map_len):
                    comp_map[d].append(map[j][k])
        else:
            if len(comp_map[(d[0]-1,d[1],d[2])]) == True:
                map1 = comp_map[(d[0]-1,d[1],d[2])][:len(comp_map[(d[0]-1,d[1],d[2])])//2]
                map2 = comp_map[(d[0]-1,d[1],d[2])][len(comp_map[(d[0]-1,d[1],d[2])])//2:]
                map1_1 = []
                map1_2 = []
                map2_1 = []
                map2_2 = []
                for j in range(len(comp_map[(d[0]-1,d[1],d[2])])//2):
                    if j % 8 < 4:
                        map1_1.append(map1[j])
                    else:
                        map1_2.append(map1[j])
                for j in range(len(comp_map[(d[0]-1,d[1],d[2])])//2):
                    if j % 8 < 4:
                        map2_1.append(map2[j])
                    else:
                        map2_2.append(map2[j])


            

 


            

