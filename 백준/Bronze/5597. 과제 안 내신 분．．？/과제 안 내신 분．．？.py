_stu = [0] * 31

for i in range(28):
  num = int(input())
  _stu[num] = 1

for i in range(1, 31):
  if _stu[i] == 0:
    print(i)