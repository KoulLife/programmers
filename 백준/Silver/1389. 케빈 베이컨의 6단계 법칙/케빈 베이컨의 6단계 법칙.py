from collections import deque

N, M = map(int, input().split())
min_val = 1e9
res = -1
adj = [[] for _ in range(N)]

for _ in range(M):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

for i in range(N):
        visited = [False] * N
        Q = deque([i])
        visited[i] = True
        A = [0] * N

        while len(Q) > 0:
                a = Q.popleft()
                for b in adj[a]:
                        if not visited[b]:
                                A[b] = A[a] + 1
                                Q.append(b)
                                visited[b] = True

        if sum(A) < min_val:
                min_val = sum(A)
                res = i + 1

print(res)