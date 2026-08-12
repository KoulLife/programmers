# BFS 문제를 풀면 방문했던 곳은 방문처리를 했는데 이 문제는 같은 곳을 또 올 수도 있지 않을까 생각해봄
# result -1의 조건은 어떻게 잡을 수 있을까
# 같은 곳을 들어오면 그냥 없애버림.
# dq에 아무 값이 없을 때, -1 
# 정답을 찾는다면 값 반환

# . D . R
# . . . .
# . G . .
# . . . D
from collections import deque

def bfs(maps, r_y, r_x, g_y, g_x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    dq = deque()
    dq.append((r_y, r_x, 0))
    maps[r_y][r_x] = 'X'
        
    while dq:
        cur_y, cur_x, cnt = dq.popleft()
        for i in range(4):
            y = cur_y + dy[i]
            x = cur_x + dx[i]
            if x < 0 or x >= len(maps[0]) or y < 0 or y >= len(maps) or maps[y][x] == 'D':
                continue
            else:                
                # 벽에 부딪힘, D에 부딪힘                    
                while True:
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y < 0 or next_y >= len(maps) or next_x < 0 or next_x >= len(maps[0]) or maps[next_y][next_x] == 'D':
                        if maps[y][x] == 'X':
                            break
                        elif x == g_x and y == g_y:
                            return cnt + 1
                        dq.append((y,x,cnt+1))
                        maps[y][x] = 'X'
                        break
                    y = next_y
                    x = next_x
                                                    
    return -1
            
def solution(board):
    maps = []
    for b in board:
        maps.append(list(b))
    
    # R의 위치, G의 위치 초기화
    r_y, r_x = -1, -1
    g_y, g_x = -1, -1
    
    # R의 위치, G의 위치 찾기
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'R':
                r_y = y
                r_x = x
            elif maps[y][x] == 'G':
                g_y = y
                g_x = x
    
    return bfs(maps, r_y, r_x, g_y, g_x)