import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []

pos1 = 0
pos2 = 0

while pos1 < N and pos2 < M:
  c1 = A[pos1]
  c2 = B[pos2]

  if c1 < c2:
    C.append(c1)
    pos1 += 1
  else:
    C.append(c2)
    pos2 += 1

if pos1 != N:
  C.extend(A[pos1:N])
if pos2 != M:
  C.extend(B[pos2:M])

print(*C)