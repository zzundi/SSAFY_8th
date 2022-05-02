num = list(map(int, input()))
dp=[0]*(len(num)+1)
dp[0] = 1
dp[1] = 1
if num[0] == 0:
    print(0)
elif len(num) <= 2:
    if (num[0] == 1 and num[1] != 0) or (0 < num[0] <= 2 and 0<num[1]<=6):
        dp[-1] = 2
    else:
        dp[-1] = 1
    print(dp[-1])
else:
    num = [0] + num
    for i in range(2, len(num)+1):
        if num[i-1] == 0:
            dp[i] = dp[i-1]
        elif (num[i-2] == 1 and num[i-1] != 0) or (num[i-2] <= 2 and 0<num[i-1] <= 6):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    print(dp[-1])
