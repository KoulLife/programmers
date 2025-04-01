S = input()
D = {}

for i in range(len(S)):
    if S[i] not in D.keys():
        D[S[i]] = i

for i in range(26):
    tmp = chr(ord('a') + i)
    if tmp in D:
        print(D[tmp],end=" ")
    else:
        print(-1,end=" ")