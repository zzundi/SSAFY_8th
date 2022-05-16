n = int(input())
num_list = list(map(int, input().split()))
reverse_num_list = list(reversed(num_list))
inc_dp = [1]*n
dec_dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j]+1)
        if reverse_num_list[i] > reverse_num_list[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j]+1)
dec_dp.reverse()
long_num = 1
for i in range(n):
    long_num = max(inc_dp[i] + dec_dp[i] -1, long_num)
print(long_num)

