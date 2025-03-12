T = int(input())
for _ in range(T):
  A, B = map(int, input().split())
  res = 0
  list_A = list(map(int, input().split()))
  list_B = list(map(int, input().split()))
  list_A.sort()
  list_B.sort()
  l, r = 0, 0
  while (l < A and r < B):
    if list_A[l] <= list_B[r]:
      l += 1
      res += r
    else:
      r += 1
  for j in range(l, A):
    res += B
  print(res)