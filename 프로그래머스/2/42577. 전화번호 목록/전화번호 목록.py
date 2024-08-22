def solution(phone_book): 

    hash_map = set()
    
    for i in phone_book: 
        hash_map.add(i) 
    
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            if arr in hash_map and arr != nums:       
                return False 
                
    return True