def solution(people, limit):
    # 최대 2명
    # greedy 사용
    # 50000 -> O(n^2) 가능
    # 80, 70, 50, 50
    
    people.sort(reverse = True)
    
    l, r = 0, len(people)-1
    res = 0
    
    while(l <= r):
        if l == r:
            res += 1
            break
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1
        res += 1
    
    return res
        