def solution(participant, completion):
    dic = {}
    
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for j in completion:
        if dic[j] == 1:
            dic.pop(j)
        elif dic[j] >= 2:
            dic[j] -= 1
    res = list(dic.keys())
    return res[0]