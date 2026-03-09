from collections import deque

def solution(maps):
    answer = -1    
    # 시작점 (0,0)에서 거리 1부터 시작 (문제 조건)
    queue = deque([ ([0, 0], 1) ])
    
    target_y = len(maps) - 1
    target_x = len(maps[0]) - 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 시작 위치도 방문 처리 (중요!)
    maps[0][0] = 0
    
    while queue:
        curr_loc, dist = queue.popleft()
        y, x = curr_loc[0], curr_loc[1]
        
        # 도착했을 때
        if y == target_y and x == target_x:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 1. 맵 범위 안에 있는지 확인
            if 0 <= ny <= target_y and 0 <= nx <= target_x:
                # 2. 벽이 아니고(1) 아직 방문하지 않았는지 확인
                if maps[ny][nx] == 1:
                    maps[ny][nx] = 0  # 다시 방문하지 않도록 벽으로 만듦
                    queue.append(([ny, nx], dist + 1))
    
    return answer