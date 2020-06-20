# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

from sys import stdin
input = stdin.readline

N = input()
nList = list(input().split())

M = input()
mList = list(input().split())

cntDic = {}
cntDic = cntDic.fromkeys(nList, 0)

resultList = []

for nNum in nList:
  if nNum in cntDic:
    cntDic[nNum] = cntDic[nNum] + 1

for mNum in mList:
  if mNum in cntDic:
    resultList.append(cntDic[mNum])
  else:
    resultList.append(0)

print(" ".join(map(str,resultList)))