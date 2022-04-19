from copy import deepcopy

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A_T = [[A[j][i] for j in range(N)] for i in range(N)]
ori_A = deepcopy(A)
I_N = [[1 if i ==j else 0 for i in range(N)] for j in range(N)]
ori_IN = deepcopy(I_N)
I_N_T = [[I_N[j][i] for j in range(N)] for i in range(N)]
remain_map = []
idx = 0
while True:
    if B >= 2:
        if B % 2 == 1:
            remain_map.append(1)
            idx += 1
        else:
            remain_map.append(0) 
            idx += 1
        B = B // 2
    else:
        break
for l in range(len(remain_map)):
    if remain_map[l] == 1:
        for i in range(N):
            for j in range(N):
                Add = []
                for k in range(N):
                    Add.append(ori_IN[i][k] * A_T[j][k])
                I_N[i][j] = sum(Add) % 1000
        ori_IN = deepcopy(I_N)
        I_N_T = [[I_N[j][i] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            Add = []
            for k in range(N):
                Add.append(ori_A[i][k] * A_T[j][k])
            A[i][j] = sum(Add) % 1000
    ori_A = deepcopy(A)
    A_T = [[A[j][i] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        Add = []
        for k in range(N):
            Add.append(ori_A[i][k] * I_N_T[j][k])
        A[i][j] = sum(Add) % 1000
for i in range(N):
    for j in range(N):
        print(A[i][j], end=' ')
    print()