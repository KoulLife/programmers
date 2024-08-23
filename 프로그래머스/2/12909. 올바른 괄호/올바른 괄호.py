def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if stack == [] or stack[-1] != '(':
                return False
            else:
                stack.pop()
                
    if stack != []:
        return False
    
    return True
    
    
    
    