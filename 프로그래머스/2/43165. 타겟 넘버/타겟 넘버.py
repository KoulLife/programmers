def dfs(numbers, target, idx, value):
    if idx == len(numbers):
        return 1 if target == value else 0
    
    count = 0
    count += dfs(numbers, target, idx+1, value+numbers[idx])
    count += dfs(numbers, target, idx+1, value-numbers[idx])
    
    return count

def solution(numbers, target):
    res = dfs(numbers, target, 0, 0)
    
    return res