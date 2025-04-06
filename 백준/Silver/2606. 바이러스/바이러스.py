import sys
input = sys.stdin.readline

com = int(input())
N = int(input())
adj = [[] for _ in range(com)]
visit = [False] * com

# adj에 값 넣기
for _ in range(N):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

def DFS(n):
    visit[n] = True
    for v in adj[n]:
        if not visit[v]:
            DFS(v)

DFS(0)

res = 0
for i in range(len(visit)):
    if visit[i] == True:
        res += 1

print(res - 1)