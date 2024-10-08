
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
def solution(line):
    points = set()
    maxX, maxY, minX, minY = -10e10, -10e10, 10e10, 10e10
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            tmp = A * D - B * C
            if tmp != 0 and (B*F-E*D)%tmp == 0 and (E*C-A*F)%tmp == 0:
                X, Y = (B*F-E*D)//tmp, (E*C-A*F)//tmp
                maxX, maxY, minX, minY = max(maxX, X), max(maxY, Y), min(minX, X), min(minY, Y)
                points.add((X, Y))
    answer = [["." for c in range(maxX-minX+1)] for r in range(maxY-minY+1)]
    for x, y in points:
        answer[maxY-y][x-minX] = "*"
    return ["".join(row) for row in answer]