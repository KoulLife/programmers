from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
res = -1
max_num = 1e9

for _ in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for i in range(N):
    dist = [-1] * N
    visit = [False] * N
    dist[i] = 0
    visit[i] = True
    queue = deque([i])

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1
    if max_num > sum(dist):
        max_num = sum(dist)
        res = i

print(res + 1)