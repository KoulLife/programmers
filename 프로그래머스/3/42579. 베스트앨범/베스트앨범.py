def solution(genres, plays):
    D1 = {}
    D2 = {}
    ans = []
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in D1:
            D1[g] = p
        else:
            D1[g] += p
        if g not in D2:
            D2[g] = [(i, p)]
        else:
            D2[g].append((i, p))
    
    # sort & [:2]
    # genre : D1
    for (D1_g, D1_p) in sorted(D1.items(), key = lambda x:x[1], reverse = True):
        for (D2_i, D2_p) in sorted(D2[D1_g], key = lambda x:x[1], reverse = True)[:2]:
            ans.append(D2_i)
    
    return ans
    