n =  int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort()
dp = [1] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j] +1:
            dp[i] += 1
print(n - max(dp))