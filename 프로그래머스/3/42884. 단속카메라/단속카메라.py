def solution(routes):
    routes = sorted(routes, key = lambda x:x[1])
    key = -30001
    ans = 0
    
    for route in routes:
        if route[0] > key:
            ans += 1
            key = route[1]
    return ans
    