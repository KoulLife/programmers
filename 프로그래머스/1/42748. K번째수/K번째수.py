def solution(array, commands):
    res = []

    for [i, j, k] in commands:
        arr = array[(i-1):j]
        arr.sort()
        res.append(arr[k-1])

    return res