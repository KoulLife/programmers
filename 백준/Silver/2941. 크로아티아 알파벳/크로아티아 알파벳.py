w = input()

dic = {'c=', 'c-', 'dz=','d-', 'lj', 'nj','s=', 'z='}
i = 0
cnt = 0

while i < len(w):
  if w[i:i+3] in dic:
    cnt += 1
    i = i + 3
  elif w[i:i+2] in dic:
    cnt += 1
    i = i + 2
  else:
    cnt += 1
    i += 1
print(cnt)