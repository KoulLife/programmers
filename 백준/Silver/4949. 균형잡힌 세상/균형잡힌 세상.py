while True:
  s = input()
  if s == ".":
    break

  stack = list()
  is_right = True
  for i in range(len(s)):
    if s[i] == '[' or s[i] == '(':
      stack.append(s[i])
    elif s[i] == ']':
      if len(stack) == 0 or stack.pop() != '[':
        is_right = False
        break
    elif s[i] == ')':
      if len(stack) == 0 or stack.pop() != '(':
        is_right = False
        break
  if len(stack) != 0:
    is_right = False

  print('yes') if is_right else print('no')