from itertools import permutations

def sosu(number):
    if number < 2:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    num_list = []
    result = []
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        num_list.extend(permutations(numbers, i))
        result = [int(''.join(n)) for n in num_list]
    
    for r in set(result):
        if sosu(r):
            answer += 1
    
    return answer