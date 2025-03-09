import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  C = []

  for i in range(N):
    a, b = map(int, input().split())
    C.append((a, b))

  C.sort()
  top = 1e9
  res = 0
  
  for j in range(N):
    if C[j][1] < top:
      res += 1
      top = C[j][1]

  print(res)
  