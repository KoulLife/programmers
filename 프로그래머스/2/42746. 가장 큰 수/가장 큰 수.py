def custom_key(x):
    return x * 3

def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=custom_key, reverse=True)
    
    res = str(''.join(num))
    return '0' if res[0] == '0' else res