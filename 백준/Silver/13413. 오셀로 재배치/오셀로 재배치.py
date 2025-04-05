# 개수는 필수, 다른 것은 2로 하면 될듯
N = int(input())

for _ in range(N):
    M = int(input())
    user = list(input())
    com = list(input())

    diff_len = 0
    diff_loc = 0
    user_B = 0
    com_B = 0

    res = 0

    for i in range(M):
        if user[i] == 'B':
            user_B += 1
        if com[i] == 'B':
            com_B += 1
        if user[i] != com[i]:
            diff_loc += 1
    diff_len = abs(user_B - com_B)
    # diff_len res에 플러스
    res += diff_len
    # diff_len 만큼 diff_loc 줄이기
    diff_loc -= diff_len
    # diff_loc / 2
    res += diff_loc // 2
    print(res)