n, m = map(int, input().split())
arr = []

def f1(start):
  if len(arr) == m:
    print(*arr)
    return

  for i in range(start, n + 1):
    arr.append(i)
    f1(i + 1)
    arr.pop()

f1(1)