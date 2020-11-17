from sys import stdin
input = stdin.readline

n = int(input())
stack = []
result = []
inputList = []
index = 0
lastStackElement = -1

def getLastStackElement():
  if (not len(stack)):
    return -1
  return stack[-1]

for i in range(n):
  inputList.append(int(input()))

for i in range(n):
  stack.append(i + 1)
  result.append('+')

  while(index < n and getLastStackElement() == inputList[index]):
    index += 1
    result.append('-')
    stack.pop()

if len(stack) > 0:
  print('NO')
else:
  for i in result:
    print(i)
