N, M = map(int, input().split())
V = list(map(int, input().split()))

# Set Range
left = max(V)
right = sum(V)

# Set Ans
ans = -1

# Set Repeat
while left <= right:
  
  # mid
  mid = (left + right) // 2
  
  num_blu = 1
  tmp = mid

  for i in range(len(V)):
    if tmp < V[i]:
      tmp = mid
      num_blu += 1
    tmp -= V[i]

  if num_blu <= M:
    right = mid - 1
    ans = mid
  else:
    left = mid + 1

print(ans)
  