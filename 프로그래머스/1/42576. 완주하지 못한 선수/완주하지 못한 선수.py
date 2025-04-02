def solution(participant, completion):
    P = {}
    C = {}
    res = ""
    
    for c in completion:
        if c not in C.keys():
            C[c] = 1
        else:
            C[c] += 1
    
    for p in participant:
        if p not in P.keys():
            P[p] = 1
        else:
            P[p] += 1
    
    for s in P.keys():
        if s not in C.keys() or P[s] != C[s]:
            res = s
            break
    return res
    