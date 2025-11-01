def solution(progresses, speeds):    
    
    arr = []
    arr2 = []
    # [7, 3, 9]
    for p, s in zip(progresses, speeds):
        tmp = (100 - p) // s
        if ((100 - p) % s ) != 0:
            tmp += 1
        arr.append(tmp)        
        
    maxNum = 0
    for i in arr:
        if i > maxNum:
            maxNum = i
            arr2.append(1)
        else:
            arr2[-1] = arr2[-1] + 1
    
    return arr2