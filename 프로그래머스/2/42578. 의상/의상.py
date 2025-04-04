def solution(clothes):
    hash_map = {}

    for cloth in clothes:
        if cloth[1] in hash_map:
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1

    res = 1

    for i in hash_map:
        res *= (hash_map[i] + 1)

    return res - 1
