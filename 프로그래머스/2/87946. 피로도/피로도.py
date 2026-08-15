def solution(k, dungeons):
    res = 0
    visited = [False] * len(dungeons)
    
    def dfs(k, cnt):
        nonlocal res
        res = max(res, cnt)
        
        for i in range(len(dungeons)):
            # 방문을 하지 않앗고, 최소 필요 피로도 보다 더 크다면
            if not visited[i] and dungeons[i][0] <= k:                
                visited[i] = True
                dfs(k - dungeons[i][1],cnt+1)
                visited[i] = False
    dfs(k,0)
    return res