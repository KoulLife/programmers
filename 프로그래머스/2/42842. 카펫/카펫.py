def solution(brown, yellow):
    res = []

    for i in range(1, yellow + 1):        
        if yellow % i != 0:
            continue
        else:
            j = yellow // i
            if ((j + 2) * 2) + (i * 2) == brown:
                res = [j + 2, i + 2]
                break
    return res