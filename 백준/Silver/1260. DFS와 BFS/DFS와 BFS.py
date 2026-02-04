from sys import stdin
from collections import deque

input = stdin.readline

N, M, start_node = map(int, input().split())
graph = [[] for _ in range(N + 1)]

dfs_visited = []
bfs_visited = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for neighbors in graph:
    neighbors.sort()

def dfs(val):
    dfs_visited.append(val)

    for neighbor in graph[val]:
        if neighbor not in dfs_visited:
            dfs(neighbor)

def bfs(val):
    queue = deque([val])

    while queue:
        current_num = queue.popleft()

        if current_num not in bfs_visited:
            bfs_visited.append(current_num)

        for neighbor in graph[current_num]:
            if neighbor not in bfs_visited:
                queue.append(neighbor)


dfs(start_node)
bfs(start_node)

print(" ".join(map(str, dfs_visited)))
print(" ".join(map(str, bfs_visited)))