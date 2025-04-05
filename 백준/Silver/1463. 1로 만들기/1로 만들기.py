N = int(input())
A = [0] * (N + 1)
A[1] = 0

for i in range(2, N + 1):
    A[i] = 1 + A[i - 1]
    if i % 3 == 0:
        A[i] = min(A[i], 1 + A[i // 3])
    if i % 2 == 0:
        A[i] = min(A[i], 1 + A[i // 2])
print(A[N])