def solution(genres, plays):
    #{g : p}
    dic1 = {}
    #{g : (1,p)}
    dic2 = {}
    
    ans = []
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = p
        else:
            dic1[g] += p
        if g not in dic2:
            dic2[g] = [(i,p)]
        else:
            dic2[g].append((i,p))
    
    for d1_g, d1_p in sorted(dic1.items(), key = lambda x:x[1], reverse = True):
        for d2_i, d2_p in sorted(dic2[d1_g], key = lambda x:x[1], reverse = True)[:2]:
            ans.append(d2_i)
    return ans