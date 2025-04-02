def solution(answers):
    ans = []
    
    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0] * 3
    
    for i in range(len(answers)):
        if answers[i] == stu_1[i % len(stu_1)]:
            scores[0] += 1
        if answers[i] == stu_2[i % len(stu_2)]:
            scores[1] += 1
        if answers[i] == stu_3[i % len(stu_3)]:
            scores[2] += 1
    
    max_score = max(scores[0], scores[1], scores[2])
    
    for i in range(len(scores)):
        if scores[i] == max_score:
            ans.append(i + 1)
    return ans