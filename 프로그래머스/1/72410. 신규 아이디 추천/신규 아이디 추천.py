def solution(new_id):
    res = ''
    
    # s1
    for val in new_id:        
        res += val.lower()
    
    # s2
    tmp_val = res
    res = ''
    for val in tmp_val:
        if val == '-' or val == '_' or val == '.' or (val>= 'a' and val <= 'z') or (val>='0' and val<='9'):
            res += val
    
    # s3
    tmp_val = res
    res = ''
    for val in tmp_val:
        if res and res[-1] == '.' and val == '.':
            continue
        res += val
    
    # s4    
    if res and res[0] == '.':
        res = res[1:]
    if res and res[-1] == '.':
        res = res[:-1]
    
    # s5
    if res == '':        
        res = "a"
    
    # s6
    if len(res) >= 16:
        res = res[:15]
        while(True):            
            if res[-1] == '.':
                res = res[:-1]
            else:
                break
        
    # s7
    if len(res) <= 2:
        while(True):
            res += res[-1]
            if len(res) >= 3:
                break
    return res