from sys import stdin
input = stdin.readline

def covertToTuple(x):
  return (int(x[1]), x[0])

# 4
# 2 1 1 0
inputCount = int(input())
inputNumList = list(map(covertToTuple, enumerate(input().split(" "))))
resultList = []

if inputCount != len(inputNumList):
  print("error")
else:
  inputNumList.reverse()
  for targetTuple in inputNumList:
    resultList.insert(targetTuple[0], targetTuple[1] + 1)

  # 4 2 1 3
  print(' '.join(str(x) for x in resultList))