def solution(n, lost, reserve):
    # 교집합 처리 (자기 자신은 빌려줄 수 없음)
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)
