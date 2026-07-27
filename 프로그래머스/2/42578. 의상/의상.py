def solution(clothes):
    
    map = {}
    
    for c_name, c_type in clothes:
        if c_type not in map:
            map[c_type] = 2
        else:
            map[c_type] = map[c_type] + 1
    
    res = 1
    
    for v in map.values():
        res *= v
    
    return res - 1