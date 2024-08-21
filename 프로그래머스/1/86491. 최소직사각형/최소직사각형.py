def solution(sizes):
    # 1. big, small을 생성 0으로 초기화
    # 2. for 루프로 sizes를 순회
    # 3. 2개 중 큰 것은 큰것과 비교, 작은 것은 작은것과 비교
    
    big, small = 0, 0
    
    for i in sizes:
        big = max(big, max(i))
        small = max(small, min(i))
    
    answer = big * small
    return answer