K = int(input())
arr = []
res = 0

for _ in range(K):
  num = int(input())
  if num == 0:
    arr.pop()
  else:
    arr.append(num)

for i in range(len(arr)):
  res += arr[i]

print(res)