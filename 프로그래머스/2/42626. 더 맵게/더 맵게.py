import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    res = -1
    mix = 0
    while True:                
        spicy_01 = heapq.heappop(scoville)
        if spicy_01 >= K:
            res = mix
            break
        
        if len(scoville) == 0:
            break
            
        spicy_02 = heapq.heappop(scoville)
        
        new_spicy = spicy_01 + (spicy_02 * 2)
        heapq.heappush(scoville ,new_spicy)        
        mix += 1
        
    return res
        
        