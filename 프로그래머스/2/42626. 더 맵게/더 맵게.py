import heapq
# [1, 2, 3, 9, 10, 12]


def solution(scoville, K):
    res = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        
        if len(scoville) < 2:
            return -1
    
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, (a + (b * 2)))
        res += 1
    
    return res