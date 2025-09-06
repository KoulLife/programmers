def solution(numbers):
    res = ""

    mappedListNums = list(map(str, numbers))
    mappedListNums.sort(key = lambda x: x*3, reverse=True)
    res = ''.join(mappedListNums)
    return str(int(res))