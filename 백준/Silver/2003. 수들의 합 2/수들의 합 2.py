import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
P = [0]
res = 0

for i in range(N):
  P.append(A[i] + P[i])
  
left, right = 0, 1

while right < len(P):
  if (P[right] - P[left]) == M:
    res += 1
    left += 1
    right += 1
  elif (P[right] - P[left]) < M:
    right += 1
  else:
    left += 1
print(res)