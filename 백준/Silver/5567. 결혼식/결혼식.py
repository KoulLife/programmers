N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

# 인접리스트 만들기
for i in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

# 체크 생성
check = [0] * N
check[0] = 1

for i in adj[0]:
    if check[i] == 0:
        check[i] = 1

    for j in adj[i]:
        if check[j] == 0:
            check[j] = 1

count = 0

for i in range(1, N):
    if check[i] == 1:
        count += 1

print(count)