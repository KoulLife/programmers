def solution(numbers, target):
    # 1. i가 len(numbers)면 비교후 종료
    # 2. v +와 - 비교
    cnt = 0
    
    def dfs(i, v):
        if i == len(numbers):
            if v == target:
                nonlocal cnt
                cnt += 1
            return
        else:
            dfs(i + 1, v + numbers[i])
            dfs(i + 1, v - numbers[i])
    dfs(0,0)
    return cnt