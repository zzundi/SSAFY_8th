n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def search(x, y):
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and Map[x][y] > Map[nx][ny]:
            dp[x][y] += search(nx, ny)
    return dp[x][y]
print(search(0, 0))

