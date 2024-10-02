import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
  a = sys.stdin.readline().split()
  
  if a == ['top']:
    if stack == []:
      print(-1)
    else:
      print(stack[-1])
    
  elif a == ['size']:
    print(len(stack))
    
  elif a == ['empty']:
    if stack == []:
      print(1)
    else:
      print(0)
      
  elif a == ['pop']:
    if stack == []:
      print(-1)
    else:
      print(stack.pop())
      
  else:
    stack.append(int(a[1]))