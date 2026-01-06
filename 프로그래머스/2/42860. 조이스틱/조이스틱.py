def solution(name):
    
    res = 0
    min_move = len(name) - 1
    
    for i, s in enumerate(name):
        res += min((ord(s) - ord('A')), (ord('Z') - ord(s) + 1))
        
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
    
    return res + min_move
    
        
        