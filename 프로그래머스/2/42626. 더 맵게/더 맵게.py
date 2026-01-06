import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    res = 0
    
    while True:
        if scoville[0] < K and len(scoville) == 1:
            res = -1
            break
        
        if scoville[0] >= K:            
            break
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        mix = a + (b * 2)
        
        heapq.heappush(scoville, mix)
        
        res += 1
    
    return res
        