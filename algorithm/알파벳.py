R, C = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [list(input()) for _ in range(R)]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
visited = {}
for alp in alpha:
    visited[alp] = False
answer = 0
def move(x, y, ans):
    global answer
    answer = max(ans, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < R and nx >= 0 and ny < C and ny >= 0 and visited[board[nx][ny]] == False:
            visited[board[nx][ny]] = True
            move(nx, ny, ans+1)
            visited[board[nx][ny]] = False
visited[board[0][0]] = True
move(0, 0, 1)
print(answer)
