n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):
    noc = []
    for j in range(1, i):
        if (i-j)%j == 0:
            noc.append(dp[j] + (i-j)//j + 1)
        else:
            noc.append(dp[j] + (i-j)//j + 2 + j*((i-j)//j+1)+j-i)
    dp[i] = min(noc)
print(dp[n])