import sys
input = sys.stdin.readline

N = int(input())
P = [0]
for i in range(N):
  P.append(int(input()))

res = 0
for j in range(N, 0, -1):
  if P[j] > P[j - 1]:
    continue
  else:
    while True:
      if P[j] > P[j - 1]:
        break
      P[j - 1] = P[j - 1] - 1
      res += 1

print(res)