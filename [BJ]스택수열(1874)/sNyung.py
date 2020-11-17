from sys import stdin
input = stdin.readline


n = int(input())
targetList = list(map(lambda x: int(input()), range(n)))
targetIdx = 0
targetCopyList = list(reversed(range(1, n + 1)))
stack = []
result = []

while len(targetCopyList) != 0:
  if len(targetCopyList) != 0:
    result.append('+')
    stack.append(targetCopyList.pop())

  while len(stack) != 0:
    targetNum = stack.pop()

    if targetList[targetIdx] == targetNum:
      targetIdx += 1
      result.append('-')
    else :
      stack.append(targetNum)
      break

if len(stack) > 0:
  print('NO')
else:
  for i in result:
    print(i)