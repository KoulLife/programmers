dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def jigae(S, D):
    # 상,하,좌,우 중 "0"이 있다 --> 0으로 & 검사기
    index = []

    for i in range(1, len(S) - 1):
        for j in range(1, len(S[0]) - 1):
            if S[i][j] == D:
                for k in range(4):
                    nx, ny = j + dx[k], i + dy[k]
                    if S[ny][nx] == '0':
                        index.append((i, j))
                        break

    for (i, j) in index:
        S[i][j] = "0"
        isOutSide(S, j, i)


def crane(S, D):
    for i in range(1, len(S) - 1):
        for j in range(1, len(S[0]) - 1):
            if S[i][j] == D:
                S[i][j] = '1'
                isOutSide(S, j, i)


def isOutSide(S, x, y):
    outside = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if S[ny][nx] == "0":
            S[y][x] = "0"
            outside = True
            break
    if outside:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if S[ny][nx] == "1":
                S[ny][nx] = "0"
                isOutSide(S, nx, ny)


def solution(storage, requests):
    # wrapped '0'
    S = [["0"] * (len(storage[0])+2) for _ in range(len(storage) + 2)]

    # insert Value
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            S[i + 1][j + 1] = storage[i][j]

    # 크레인(길이 2), 지게차(길이 1) 구분
    for r in requests:
        if len(r) == 1:
            # 지게차
            jigae(S, r)
        else:
            # 크레인
            crane(S, r[0])

    res = 0
    for i in range(1, len(S) - 1):
        for j in range(1, len(S[0]) - 1):
            if S[i][j] not in ['0', '1']:
                res += 1

    return res