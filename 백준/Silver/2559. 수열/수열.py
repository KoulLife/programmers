N, M = map(int, input().split())
A = list(map(int, input().split()))
res = -1e9

# 누적합 만들기
pSum = [0] * (N+1)
pSum[0] = 0
for i in range(1, N+1):
    pSum[i] = pSum[i-1] + A[i-1]
# 시작 지점 확인
for i in range(M, N+1):
    res = max(res, pSum[i] - pSum[i - M])

print(res)