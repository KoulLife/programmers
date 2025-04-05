from collections import deque

def solution(priorities, location):
        S = []  # 값 초기화
        max_arr = []  # 최댓값 확인 배열

        for i, v in enumerate(priorities):
                S.append([i, v])  # [[0,2], [1,1], [2,3], [3,2]]
                max_arr.append(v)
        max_arr.sort(reverse=True)  # [3,2,2,1]
        Q = deque(S)
        idx = 0

        while len(Q) > 0:
                [i, v] = Q.popleft()
                if v == max_arr[0]:
                        idx += 1
                        max_arr.pop(0)
                        if i == location:
                                break
                else:
                        Q.append([i, v])

        return idx