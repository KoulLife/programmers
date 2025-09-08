def solution(number, k):
    S = []
    
    for num in number:
        while S and k > 0 and S[-1] < num:
            S.pop()
            k -= 1
        S.append(num)
    
    return ''.join(S[:len(S) - k])
    