N, M = map(int, input().split())
AM = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0]*(sum(C)+1) for _ in range(N+1)]
result = sum(C)
for i in range(1, N+1):
    for j in range(len(dp[1])):
        if C[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-C[i]] + AM[i], dp[i-1][j])
        if dp[i][j] >= M:
            
            result = min(result, j)
if M != 0:
    print(result)

else:
    print(0)