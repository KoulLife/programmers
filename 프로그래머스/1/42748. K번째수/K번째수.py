def solution(array, commands):
    # 1. for 문으로 commands를 순회
    # 2. 0, 1, 2를 i, j, k로 넣기
    # 3. i ~ j 만큼 array 자르기
    # 4. 정렬하기
    # 5. k 요소 res에 넣기
    res = []
    
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        
        arr = array[i - 1 : j]
        arr.sort()
        res.append(arr[k - 1])
    
    return res