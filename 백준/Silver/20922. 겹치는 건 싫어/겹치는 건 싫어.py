from sys import stdin
from collections import defaultdict

def solution(N, K, A):
    answer = 0
    left, right = 0, 0
    counts = defaultdict(int)

    while right < N:
        if counts[A[right]] >= K:
            counts[A[left]] -= 1
            left += 1
        else:
            counts[A[right]] += 1
            right += 1
            answer = max(answer, right - left)
    return answer

N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

result = solution(N, K, A)
print(result)