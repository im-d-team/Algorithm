import sys
from itertools import permutations
input = sys.stdin.readline

count = 0
checkList = []
inputCount = int(input())

for _ in range(inputCount):
  checkList.append(tuple(map(int, input().rstrip().split())))

for dNum in list(permutations([1,2,3,4,5,6,7,8,9], 3)):
  flag = True
  for targetNum, targetStrike, targetBall in checkList:
    ball = 0
    strike = 0
    
    for i in range(3):
      for j, tNum in enumerate(str(targetNum)):
        if i==j and dNum[i] == int(tNum):
          strike += 1
        elif dNum[i] == int(tNum):
          ball += 1
    if targetBall != ball or targetStrike != strike :
      flag = False
      break

  if flag :
    count = count + 1

print(count)