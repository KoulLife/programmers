def solution(s):    
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append('(')
        else:
            if stack == []:
                return False
            else:
                stack.pop(-1)
    if len(stack) == 0:
        return True
    else:
        return False    