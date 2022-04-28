n = int(input())
dp = [1] * n
kids_num = [int(input()) for _ in range(n)]
for i in range(n):
    print()
    for j in range(i):
        if kids_num[i] > kids_num[j]:
            dp[i] += 1
print(n - max(dp))