def solution(diffs, times, limit):
#     diff <= level
#         times[i]
    
#     diff > level
#         (times[i] + times[i - 1]) * (diff[i] - level) + times[i]
        
#     2. 돌려보고 limit 넘어가기 직전의 level 리턴
    res = 0
    maxL, minL = max(times), min(times)
    
    for level in range(maxL, minL - 1, -1):
        tmp = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                tmp += times[i]
            elif diffs[i] > level:
                tmp += (times[i] + times[i - 1]) * (diffs[i] - level) + times[i]
        if tmp <= limit:
            res = level
        elif tmp > limit:
            return level
    
    return level
        