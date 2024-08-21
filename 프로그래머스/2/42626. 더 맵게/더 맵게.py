import heapq

def solution(scoville, K):
    res = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        mix = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix)
        res += 1
        
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    
    return res