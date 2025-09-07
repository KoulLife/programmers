def solution(answers):    
    # 학생의 찍기 패턴 적용
    pattern_s1 = [1, 2, 3, 4, 5]
    pattern_s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 학색 점수 초기화    
    c_s1 = 0
    c_s2 = 0
    c_s3 = 0
    
    # 점수 for문 확인, 
    for i in range(len(answers)):
        if answers[i] == pattern_s1[i%len(pattern_s1)]:
            c_s1 += 1
        if answers[i] == pattern_s2[i%len(pattern_s2)]:
            c_s2 += 1
        if answers[i] == pattern_s3[i%len(pattern_s3)]:
            c_s3 += 1
    
    score_list = [c_s1, c_s2, c_s3]
    
    max_score = 0
    res = []
    for [i, score] in enumerate(score_list):
        if score > max_score:
            max_score = score
            res = [i + 1]
        elif score == max_score:
            res.append(i + 1)
                
    return res