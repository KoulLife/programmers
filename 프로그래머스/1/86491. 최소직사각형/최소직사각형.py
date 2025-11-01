def solution(sizes):
    for size in sizes:
        size.sort(reverse = True)
    
    maxW = 0
    maxH = 0
    
    for size in sizes:
        if maxW <= size[0]:
            maxW = size[0]
        if maxH <= size[1]:
            maxH = size[1]
            
    return maxW * maxH