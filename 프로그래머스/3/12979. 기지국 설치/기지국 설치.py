def solution(n, stations, w):
    answer = 0
    cover = w * 2 + 1
    start = 1
    
    for station in stations:
        left = station - w
        if start < left:
            gap = left - start
            answer += (gap + cover - 1) // cover
        start = station + w + 1
    
    if start <= n:
        answer += (n - start + cover) // cover

    return answer