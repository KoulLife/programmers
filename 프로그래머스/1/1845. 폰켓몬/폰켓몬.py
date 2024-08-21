def solution(nums):
    dic = set()

    for _ in nums:
        dic.add(_)

    if len(nums) / 2 <= len(dic):
        return len(nums) / 2
    else:
        return len(dic)
    