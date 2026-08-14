def solution(nums):
    res = 0
    for n1 in range(len(nums)-2):
        for n2 in range(n1+1,len(nums)-1):
            for n3 in range(n2+1,len(nums)):
                num = nums[n1] + nums[n2] + nums[n3]                
                is_sosu = True
                for i in range(2, num):
                    if num % i == 0:
                        is_sosu = False
                        break
                if is_sosu:
                    res += 1
    return res
    