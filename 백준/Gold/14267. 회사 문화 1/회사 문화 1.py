N, M = map(int, input().split())
P = list(map(int, input().split()))

for i in range(1, N):
  P[i] -= 1

good = [0] * N
for i in range(M):
  I, W = map(int, input().split())
  good[I-1] += W

res = [0] * N
for i in range(1, N):
  res[i] = res[P[i]] + good[i]

print(*res)