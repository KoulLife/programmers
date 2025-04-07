p, w = map(int, input().split())
N = list(input())

# 배열 생성
words = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]

# 이전에 누른 키의 인덱스를 저장할 변수 (리스트 사용)
prev_key = None
res = 0

for char in N:
    if char == " ":
        # 공백은 한 번 누르는 경우
        res += p
        prev_key = None  # 공백 후에는 대기 시간 없음
    else:
        # 해당 문자가 몇 번째 키에 있는지와 몇 번 눌러야 하는지 확인
        for i, key_group in enumerate(words):
            if char in key_group:
                # 만약 이전 문자와 같은 키라면 대기 시간 추가
                if prev_key is not None and prev_key == i:
                    res += w
                # 해당 키에서 몇 번 눌러야 하는지 (인덱스+1)
                presses = key_group.index(char) + 1
                res += presses * p
                prev_key = i
                break

print(res)
