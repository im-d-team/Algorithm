from sys import stdin
input = stdin.readline

count = int(input())
topList = list(map(int, input().split(" ")))
topStack = []
resultList = []

for idx, targetNum in enumerate(topList):
  if(len(topStack) == 0):
    topStack.append((idx, targetNum))
    resultList.append('0')
    continue

  while topStack:
    topTuple = topStack.pop()
    
    if(targetNum <= topTuple[1]):
      resultList.append(str(topTuple[0] + 1))
      topStack.append(topTuple)
      topStack.append((idx, targetNum))
      break
    elif(len(topStack) == 0):
      topStack.append((idx, targetNum))
      resultList.append('0')
      break
print(" ".join(resultList))