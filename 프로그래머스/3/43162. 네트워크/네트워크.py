def solution(n, computers):    
    # 인접리스트 생성
    adj = [[] for _ in range(n)]
    
    for idx, computer in enumerate(computers):
        for i, c in enumerate(computer):
            if i != idx and c == 1:
                adj[idx].append(i)
    
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer