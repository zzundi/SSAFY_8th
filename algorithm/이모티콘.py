n = int(input())
dp = [0]*(n+1)
for i in range(2, n+1):
    noc = []
    for j in range(1, i):
        f = dp[j] + (i-j)//j
        if (i-j)%j == 0:
            noc.append(f + 1)
        else:
            noc.append(f + 2 + j*((i-j)//j+2)-i)
    dp[i] = min(noc)
print(dp[n])