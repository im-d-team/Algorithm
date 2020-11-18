# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

from sys import stdin
input = stdin.readline

testCaseCount = int(input())  
result = []
for i in range(testCaseCount):
  left = []
  right = []
  inputList = list(input().rstrip())

  for j in range(len(inputList)):
    if inputList[j] == '<':
      if len(left):
        right.append(left.pop())
    elif inputList[j] == '>':
      if len(right):
        left.append(right.pop())    
    elif inputList[j] == '-':
      if len(left):
        left.pop()
    else:
      left.append(inputList[j])

  result.append(''.join(left) + ''.join(reversed(right)))

for data in result:
  print(data)