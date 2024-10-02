n = int(input())
arr = []
res = 0

for _ in range(n):
  arr.append(input())

for i in arr:
  stack = []
  check = True
  for j in i:
    if stack == [] or stack[-1] == j:
      stack.append(j)
    elif stack[-1] != j:
      if j in stack:
        check = False
        break
      else:
        stack.append(j)
  if check == True:
    res += 1

print(res)