def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append('(')
        else:
            if not stack or stack.pop(-1) == ')':
                return False                                        
        
    return True if not stack else False