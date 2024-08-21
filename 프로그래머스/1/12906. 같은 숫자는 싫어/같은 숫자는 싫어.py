def solution(arr):
    res = []
    
    for i in range(0, len(arr)):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        else:
            res.append(arr[i])
    
    
    return res