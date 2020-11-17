from sys import stdin
input = stdin.readline

caseCount = int(input())
caseList = list(map(lambda x: input().strip(), range(caseCount)))
resultList = []

for case in caseList:
  result = ''
  leftStack = []
  rightStack = []

  for char in case:
    if char == '<' :
      # 왼쪽이 있다면 왼쪽 하나를 오른쪽으로 
      len(leftStack) != 0 and rightStack.append(leftStack.pop())
    elif char == '>':
      # 오른쪽이 있다면 오른쪽 하나를 오른쪽으로 
      len(rightStack) != 0 and leftStack.append(rightStack.pop())
    elif char == '-':
      len(leftStack) != 0 and leftStack.pop()
    else :
      leftStack.append(char)
  resultList.append(''.join(leftStack) + ''.join(reversed(rightStack)))

for r in resultList:
  print(r)

