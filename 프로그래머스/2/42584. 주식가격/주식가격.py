from collections import deque

def solution(prices):
    Q = deque(prices)
    res = []
    
    while Q:
        u = Q.popleft()
        period = 0
        for after in Q:
            period += 1
            if u > after:
                break
        res.append(period)
    return res