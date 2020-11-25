from sys import stdin
input = stdin.readline

nCount = int(input())
nArr = list(map(int, input().split(' ')))
mCount = int(input())
mArr = list(map(int, input().split(' ')))

nCountDic = {}
resultArr = []

for i in nArr:
  if not i in nCountDic:
    nCountDic[i] = 1
  else:
    nCountDic[i] += 1

for j in mArr:
  if not j in nCountDic:
    resultArr.append(0)
  else:
    resultArr.append(1)

for r in resultArr:
  print(r)
