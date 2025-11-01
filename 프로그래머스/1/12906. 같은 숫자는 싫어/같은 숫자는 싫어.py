def solution(arr):
    s = []
    
    for i in arr:
        if s == [] or s[-1] != i:
            s.append(i)
    
    return s