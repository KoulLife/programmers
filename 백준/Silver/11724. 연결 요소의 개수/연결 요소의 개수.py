import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
        a, b = map(int,input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

res = 0

for i in range(N):
        if visited[i]:
                continue

        res += 1

        Q = deque([i])
        visited[i] = True

        while len(Q) > 0:
                u = Q.popleft()

                for v in adj[u]:
                        if not visited[v]:
                                visited[v] = True
                                Q.append(v)

print(res)