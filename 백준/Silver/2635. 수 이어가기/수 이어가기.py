n = int(input())

longest = []
for i in range(1, n + 1):
    numbers = [n, i]
    while numbers[-1] >= 0:
        numbers.append(numbers[-2] - numbers[-1])
    numbers.pop(-1)

    if len(numbers) > len(longest):
        longest = numbers[:]
print(len(longest))
print(*longest)
