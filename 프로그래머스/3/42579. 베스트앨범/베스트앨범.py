def solution(genres, plays):
    ans = []
    dict1 = {}
    dict2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict1:
            dict1[g] = [(i, p)]
        else:
            dict1[g].append((i, p))
        if g not in dict2:
            dict2[g] = p
        else:
            dict2[g] += p

    for (k, v) in sorted(dict2.items(), key=lambda x: x[1], reverse=True):
        cnt = 0
        for (i, p) in sorted(dict1[k], key=lambda x: x[1], reverse=True):
            if cnt == 2:
                break
            ans.append(i)
            cnt += 1
    return ans