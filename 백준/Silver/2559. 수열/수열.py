import sys
input = sys.stdin.readline

N, K = map(int, input().split())
T = list(map(int, input().split()))
pSum = [0] * N
pSum[0] = T[0]

# prefix sum
for i in range(1, N):
  pSum[i] = pSum[i - 1] + T[i]

res = []
for j in range(0, N - K + 1):
  if j == 0:
    sum = pSum[j + K - 1]
  else:
    sum = pSum[j + K -1] - pSum[j - 1]
  res.append(sum)
print(max(res))