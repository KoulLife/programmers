def solution(s):
    cnt = 0
    res = ''
    for c in s:
        if c == ' ':
            cnt = 0
            res += c
        else:
            if cnt % 2 == 0:
                res += c.upper()                
            else:
                res += c.lower()
            cnt += 1
    return res