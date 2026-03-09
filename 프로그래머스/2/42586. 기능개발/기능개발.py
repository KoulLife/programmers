def solution(progresses, speeds):
    # 소요기간 계산하기
    work_arr = [0] * len(speeds)

    for i in range(len(speeds)):
        quotient = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            quotient += 1
        work_arr[i] = quotient

    answer = [0]
    max_num = 0

    for work in work_arr:
        if max_num >= work:
            answer[-1] += 1            
        else:
            answer.append(1)
            max_num = work
    answer.pop(0)
    return answer