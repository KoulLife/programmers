from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    for i, j in edge:
        adj[i].append(j)
        adj[j].append(i)
    
    distance = [-1] * (n + 1)
    distance[1] = 0
    queue = deque([ 1 ])
    
    while queue:
        no = queue.popleft()
        for neighbor in adj[no]:
            if distance[neighbor] == -1:
                queue.append( neighbor )
                distance[neighbor] = distance[no] + 1
    
    cnt = 0
    
    for d in distance:
        if d == max(distance):
            cnt += 1
    
    return cnt