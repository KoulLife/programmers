def solution(clothes):
    hashMap = {}
    
    for [a, b] in clothes:
        if b in hashMap:
            hashMap[b] += 1
        else:
            hashMap[b] = 1
    
    res = 1
    
    for _, v in hashMap.items():
        res *= (v + 1)
    
    return res - 1
        