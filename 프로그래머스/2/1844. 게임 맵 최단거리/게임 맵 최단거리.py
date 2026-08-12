from collections import deque

def bfs(boards):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    dq = deque()
    dq.append((0,0,1))
    boards[0][0] = 0
    
    while dq:
        before_y,before_x, cnt = dq.popleft()
        for i in range(4):
            y = before_y + dy[i]
            x = before_x + dx[i]
            if y < 0 or y >= len(boards) or x < 0 or x >= len(boards[0]) or boards[y][x] == 0:
                continue
            elif y == len(boards)-1 and x == len(boards[0])-1:
                return cnt + 1
            else:
                boards[y][x] = 0
                dq.append((y,x,cnt+1))
    return -1

def solution(maps):
    boards = []
    for m in maps:
        boards.append(list(m))
    
    return bfs(boards)