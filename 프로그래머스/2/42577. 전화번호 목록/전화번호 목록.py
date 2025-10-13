def solution(phone_book):
    
    hashMap = {}
    
    for nums in phone_book:
        hashMap[nums] = 1
    
    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num
            if arr in hashMap and arr != nums:
                return False
        
    return True