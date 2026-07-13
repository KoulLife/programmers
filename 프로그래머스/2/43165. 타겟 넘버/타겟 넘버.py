# 방법1: -를 1개부터 len(numbers)까지 모두 넣어서 확인한다.
# num이랑 자릿수를 넘긴다 --> 마지막 len이면서 target과 같을때 +1을 한다
res = 0
def solution(numbers, target):    
    def dfs(val, idx):                
        global res
        if idx == len(numbers):
            if val == target:
                res += 1
        else:
            dfs(val-numbers[idx], idx + 1)
            dfs(val+numbers[idx], idx + 1)
    
    dfs(0, 0)
    return res
                
        