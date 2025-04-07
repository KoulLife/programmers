P, W = map(int, input().split())
N = list(input())

# 배열 생성
words = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I'],
    ['J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T','U','V'],
    ['W','X','Y','Z']]

# 반복, 전과 비교
before = None
res = 0
for num in N:
    # 공백인지 확인, 공백이라면 before 빼고, +2
    if num == " ":
        before = None
        res += P
    else:
        for i, w in enumerate(words):
            if num in w:
                # 몇번째에 있는지 확인하기
                for tmp in w:
                    res += P
                    if tmp == num:
                        break

                # before와 비교하여 i가 같다면 10을 더하고, 비어있다면 그냥 추가하기
                if before == None:
                    before = i
                else:
                    if before == i:
                        res += W
                    before = i
print(res)