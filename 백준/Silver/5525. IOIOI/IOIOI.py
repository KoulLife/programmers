N = int(input())
M = int(input())
S = input()

Pn = "I"
Pn_cnt = 1

for i in range(N):
    Pn += "OI"
    Pn_cnt += 2

hash_val = hash(Pn)

cnt = 0

for i in range(M - Pn_cnt + 1):
    tmp = S[i:i+Pn_cnt]
    if hash(tmp) == hash_val:
        cnt += 1

print(cnt)