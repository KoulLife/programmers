def solution(k, tangerine):    
    hash_set = {}
    
    for t in tangerine:
        if t in hash_set:
            hash_set[t] += 1
        else:
            hash_set[t] = 1
    
    sorted_desc = dict(sorted(hash_set.items(), key=lambda x : x[1], reverse=True))
    
    res = 0
    for val in sorted_desc.values():
        if k <= 0:
            break
        k -= val
        res += 1
    
    return res