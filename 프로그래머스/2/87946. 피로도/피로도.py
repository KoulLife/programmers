def solution(k, dungeons):
    res = 0
    visited = [False] * len(dungeons)
    
    def dfs(current_k, count):
        nonlocal res
        res = max(count, res)
        
        for i in range(len(dungeons)):
            if dungeons[i][0] <= current_k and not visited[i]:
                visited[i] = True
                dfs(current_k - dungeons[i][1] , count + 1)
                visited[i] = False
    
    dfs(k, 0)
    return res