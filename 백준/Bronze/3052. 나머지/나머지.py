A = []
for _ in range(10):
    T = int(input())
    if T % 42 not in A:
        A.append(T % 42)
print(len(A))