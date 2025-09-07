def solution(brown, yellow):
    res = []

    for y in range(1, yellow + 1):
        if yellow % y != 0:
            continue

        x = yellow // y
        tmp = (x + 2) * 2 + (y + 2) * 2
        if (tmp) == brown + 4:
            res = [x + 2, y + 2]
            break

    return res