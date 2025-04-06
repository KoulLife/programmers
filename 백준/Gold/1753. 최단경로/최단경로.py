# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) - 1

adj = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u - 1].append((v - 1, w))

# 다익스트라
dist = [1e9] * V
Q = PriorityQueue()
dist[K] = 0
Q.put((0, K))

while Q.qsize() != 0:
    a, b = Q.get()

    if a != dist[b]:
        continue

    for v, w in adj[b]:
        if dist[v] > dist[b] + w:
            dist[v] = dist[b] + w
            Q.put((dist[v], v))

for i in range(len(dist)):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])