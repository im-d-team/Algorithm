# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

from sys import stdin
input = stdin.readline

count = int(input())

for _ in range(count):
  stack = []
  lastStack = []
  inputArr = list(input().rstrip())

  for i in inputArr:
    if i == "(":
      stack.append(i)
    else:
      if len(stack):
        stack.pop()
      else:
        lastStack.append(i)

  if (len(lastStack) or len(stack)):
    print("NO")
  else:
    print("YES")