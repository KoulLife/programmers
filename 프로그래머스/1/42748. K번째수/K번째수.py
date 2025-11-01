def solution(array, commands):
    answer = []        
    
    for i,j,k in commands:
        copiedArray = array[i-1:j]
        copiedArray.sort()
        answer.append(copiedArray[k-1])
    
    return answer