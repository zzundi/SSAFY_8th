num = list(map(int, input()))
dp=[0]*(len(num)+1)
dp[0] = dp[1] = 1
if num[0] == 0:
    print(0)
else:
    num = [0] + num
    for i in range(2, len(num)):
        if num[i-1] == num[i] == 0:
            dp[-1] = 0
            break
        if 0 < num[i]:
            dp[i] += dp[i-1]
        if num[i-1] == 1 or (num[i-1]==2 and 0 < num[i] <= 6):
            dp[i] += dp[i-2]
        elif num[i-1]<=2 and num[i] == 0:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    print(dp[-1])
