from collections import deque
import math
N, L, R = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
c_map = [list(map(int, input().split())) for _ in range(N)]
def search(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    union = [(i, j)]
    count = c_map[i][j]
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visit[nx][ny]:
                continue
            if L <= abs(c_map[nx][ny] - c_map[x][y]) <= R:
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += c_map[nx][ny]
    for x, y in union:
        c_map[x][y] = int(count/len(union))
    return len(union)
result = 0
while True:
    visit = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if search(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1
print(result)