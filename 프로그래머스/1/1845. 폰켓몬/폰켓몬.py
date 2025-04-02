def solution(nums):
    p_hash = {}
    
    for i in nums:
        if i not in p_hash.keys():
            p_hash[i] = 1
    
    return min(len(nums) // 2, len(p_hash))