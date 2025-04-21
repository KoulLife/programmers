B = input().split('.')
ans = []

for part in B:
    length = len(part)
    if length % 2 != 0:
        print(-1)
        exit()
    a_count = length // 4
    b_count = (length % 4) // 2
    ans.append('AAAA' * a_count + 'BB' * b_count)

print('.'.join(ans))