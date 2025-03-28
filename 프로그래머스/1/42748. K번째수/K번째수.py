def solution(array, commands):
    res = []
    # commands의 갯수만큼
    for C in commands:
        # array 복사한 c_array
        c_array = array[:]
        c_array = c_array[C[0]-1:C[1]]
        c_array.sort()
        res.append(c_array[C[2] - 1])
    
    return res