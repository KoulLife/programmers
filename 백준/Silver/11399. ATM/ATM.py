import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()
pArr = [0]
pSum = 0

for i in range(N):
  pArr.append(pSum + P[i])
  pSum = pArr[-1]

res = sum(pArr)
print(res)