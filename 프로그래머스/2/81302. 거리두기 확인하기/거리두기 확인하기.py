# P의 좌표를 모으고, 각 좌표별로 BFS를 돌린다.
# P의 거리가 2 이하에 암것도 없으면 1
# 뭔가가 걸린다면 0
import copy
from collections import deque

def bfs(room, p_list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for y, x in p_list:
        c_room = copy.deepcopy(room)
        dq = deque()
        dq.append((y,x,0))    
        c_room[y][x] = 'X'
        while dq:
            y, x, cnt = dq.popleft()
            if cnt >= 2:
                break
            for i in range(4):
                after_y = y + dy[i]
                after_x = x + dx[i]
                if after_y < 0 or after_y >= len(c_room) or after_x < 0 or after_x >= len(c_room[0]) or c_room[after_y][after_x] == 'X':
                    continue
                elif c_room[after_y][after_x] == 'P':
                    return 0
                else:
                    c_room[after_y][after_x] = 'X'
                    dq.append((after_y, after_x, cnt + 1))
    return 1
        

def solution(places):
    # room을 만든다 
    rooms = []
    res = []
    for place in places:
        p_list = []
        for p in place:
            p_list.append(list(p))
        rooms.append(p_list)
    
    for room in rooms:
        # p의 좌표 모으기
        p_list = []
        for y in range(len(room)):
            for x in range(len(room[0])):
                if room[y][x] == 'P':
                    p_list.append((y,x))
        val = bfs(room, p_list)
        res.append(val)
    
    return res