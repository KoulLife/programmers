def solution(genres, plays):
    dict1 = {}
    dict2 = {}
    res = []
    
    for i,(g,p) in enumerate(zip(genres, plays)):
        if g not in dict1:
            dict1[g] = [(i, p)]
        else:
            dict1[g].append((i, p))
        if g not in dict2:
            dict2[g] = p
        else:
            dict2[g] += p
    
    for (k, v) in sorted(dict2.items(), key=lambda x:x[1], reverse = True):
        for (i, p) in sorted(dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            res.append(i)
    return res
    