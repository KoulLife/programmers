# 10 5
# 1 2 3 4 2 5 3 1 1 2

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum_val = nums[0]
l, r = 0, 0
res = 0

while r < N:
    if sum_val == M:
        res += 1

    if (l <= r) and (sum_val > M):
        sum_val -= nums[l]
        l += 1
    else:
        if (r + 1) == N:
            break
        r += 1
        sum_val += nums[r]

print(res)

