C = int(input())

dp = [1e9] * (C + 1)
dp[0] = 0

for i in range(1, C + 1):
    if i >= 2:
        dp[i] = min(dp[i], 1 + dp[i - 2])
    if i >= 5:
        dp[i] = min(dp[i], 1 + dp[i - 5])

if dp[C] == 1e9:
    print(-1)
else:
    print(dp[C])