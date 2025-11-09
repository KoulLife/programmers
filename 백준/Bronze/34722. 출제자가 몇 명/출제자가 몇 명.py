N = int(input())
people = 0

for i in range(N):
    line = input()
    parts = line.split()
    n1, n2, n3, n4 = map(int, parts)

    if n1 < 1000 and n2 < 1600 and n3 < 1500 and (n4 > 30 or n4 == -1):
        continue
    else:
        people += 1

print(people)