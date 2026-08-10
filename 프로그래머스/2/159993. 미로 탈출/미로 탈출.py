from collections import deque
import copy

def bfs(original_maps, x, y, target_x, target_y):
    maps = copy.deepcopy(original_maps)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((x, y, 0))
    maps[y][x] = 'X'
    
    while dq:
        cur_x, cur_y, cnt = dq.popleft()        
        for i in range(4):
            tmp_x = cur_x + dx[i]
            tmp_y = cur_y + dy[i]
            if tmp_x < 0 or tmp_y < 0 or tmp_x >= len(maps[0]) or tmp_y >= len(maps) or maps[tmp_y][tmp_x] == 'X':
                continue
            else:
                if tmp_y == target_y and tmp_x == target_x:
                    return cnt + 1
                maps[tmp_y][tmp_x] = 'X'
                dq.append((tmp_x, tmp_y, cnt + 1))
    return -1


def solution(maps):
    # 지도를 만들기
    m_maps = []
    for m in maps:
        m_maps.append(list(m))

    # 시작 좌표, 레버 좌표, 종료 좌표 초기화
    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0
    exit_x, exit_y = 0, 0

    # 시작 좌표, 레버 좌표, 종료 좌표 찾기
    for y in range(len(m_maps)):
        for x in range(len(m_maps[0])):
            if m_maps[y][x] == 'S':
                start_x = x
                start_y = y
            elif m_maps[y][x] == 'L':
                lever_x = x
                lever_y = y
            elif m_maps[y][x] == 'E':
                exit_x = x
                exit_y = y

    a = bfs(m_maps, start_x, start_y, lever_x, lever_y)
    b = bfs(m_maps, lever_x, lever_y, exit_x, exit_y)

    if a == -1 or b == -1:
        return -1
    else:
        return a + b