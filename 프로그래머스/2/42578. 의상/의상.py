def solution(clothes):
    
    closet = {}
    
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
    
    ans = 1
    
    for _, val in closet.items():
        ans *= (len(val) + 1)
    
    return ans - 1
    