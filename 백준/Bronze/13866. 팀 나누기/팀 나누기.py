min_val = 10001
max_val = 0
sum_val = 0

arr = list(map(int, input().split()))  # 한 줄로 입력받기
n = len(arr)  # 입력받은 숫자의 개수 확인

for num in arr:
    sum_val += num
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

res = abs(sum_val - (max_val + min_val)) - (max_val + min_val)
res = abs(res)  # 절대값 계산

print(res)
