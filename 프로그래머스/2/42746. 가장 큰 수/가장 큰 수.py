def solution(numbers):
    ans = ""
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    for i in numbers:
        ans += i
    return str(int(ans))