def solution(n, costs):
    # w기준으로 오름차순 하기
    costs.sort(key = lambda x:x[2])
    # 배열 추가하기
    link = set([costs[0][0]])
    # 정답 초기화
    res = 0
    # 하나씩 빼기
    while len(link) != n:
        for u1, u2, w in costs:
            if u1 in link and u2 in link:
                continue
            if u1 in link or u2 in link:
                res += w
                link.update([u2,u1])
                break
    return res
    