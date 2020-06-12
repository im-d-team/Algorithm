# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

from sys import stdin
from operator import eq

input = stdin.readline
resultArr = []

numberCardCount = int(input())
numberCardArr = list(map(int, input().split(' ')))
userCardCount = int(input())
userCardArr = list(map(int, input().split(' ')))

countDict = {}
resultArr = []

for i in numberCardArr:
  if not i in countDict:
    countDict[i] = 1
  else:
    countDict[i] += 1

for j in userCardArr:
  if j in countDict:
    resultArr.append(countDict[j])
  else:
    resultArr.append(0)

print(" ".join(map(str, resultArr)))