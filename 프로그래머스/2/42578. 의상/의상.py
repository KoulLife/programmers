def solution(clothes):
    dict = {}
    res = 1
    
    for item, typ in clothes:
        if typ not in dict:
            dict[typ] = 1
        else:
            dict[typ] += 1
    
    arr = list(dict.values())
    
    for i in arr:
        res *= (i + 1)
    
    return res - 1