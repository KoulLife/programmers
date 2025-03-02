arr = list()
res = list()

for _ in range(10):
  num = int(input())
  arr.append(num % 42)

for i in range(10):
  if arr[i] not in res:
    res.append(arr[i])

print(len(res))