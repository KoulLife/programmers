def solution(citations):
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        h = n - i              # 남은 논문 수
        if citations[i] >= h:  # 이 시점에서 h-index 만족
            return h
    return 0
