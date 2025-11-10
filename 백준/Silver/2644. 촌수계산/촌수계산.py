import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n)]
visit = [False] * n

# 방문 계산
for _ in range(m):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)

min_chonsu = -1

# dfs로 접근하면서 계산을 해야 함
def dfs(v, chonsu):
    visit[v] = True
    global min_chonsu

    if v == (p2 - 1):
        min_chonsu = chonsu
        return

    for neighbor in adj[v]:
        if not visit[neighbor]:
            dfs(neighbor, chonsu + 1)
            if min_chonsu != -1:
                return

dfs(p1 - 1, 0)

print(min_chonsu)