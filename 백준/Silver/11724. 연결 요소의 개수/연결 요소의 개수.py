import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())
visit = [False] * N
adj = [[] for _ in range(N)]
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for i in range(N):
    if visit[i]:
        continue

    count += 1
    queue = deque([i])
    visit[i] = True

    while len(queue) != 0:
        u = queue.popleft()
        for v in adj[u]:
            if not visit[v]:
                visit[v] = True
                queue.append(v)

print(count)