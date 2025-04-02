def solution(s):
    s_dict = {')' : '('}
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0 or stack.pop() != s_dict[s[i]]:
                return False
    if len(stack) != 0:
        return False
    else:
        return True