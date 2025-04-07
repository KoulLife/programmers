def solution(n, costs):
    res = 0
    # w으로 정렬
    costs.sort(key=lambda x: x[2])

    # set 만들기
    link = set()
    link.add(costs[0][0])

    # while
    while len(link) != n:
        # costs에서 [0], [1] 값 빼기
        for u1, u2, w in costs:
            if u1 in link and u2 in link:
                continue
            if u1 in link or u2 in link:
                link.update((u1, u2))
                res += w
                break
    return res