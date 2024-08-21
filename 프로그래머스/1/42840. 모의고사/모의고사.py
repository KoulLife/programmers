def solution(answers):
#     1. 학생의 찍기 배열로 저장
#     2. a1,a2,a3 (학생 점수 저장)
#     3. for 루프로 answer 순회
#     4. a1 ~ a3까지의 값 비교
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    res = []
    score = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]: score[0] += 1
        if answers[i] == s2[i % len(s2)]: score[1] += 1
        if answers[i] == s3[i % len(s3)]: score[2] += 1
    
    tmp = max(score)
    
    for j in range(len(score)):
        if score[j] == tmp:
            res.append(j + 1)
    
    return res