import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
res = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def DFS(n):
    visit[n] = True
    for leaf in adj[n]:
        if not visit[leaf]:
            res[leaf] = n
            DFS(leaf)

DFS(1)  # 루트 노드가 1번!

for i in range(2, N + 1):
    print(res[i])
