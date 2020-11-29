import copy
from sys import stdin
input = stdin.readline

F = int(input())
resultList = []

def checkRelation(rList, name):
  print('checkRelation', rList, name)
  
  while len(rList[name]) > 0:
    tName = rList[name].pop()
    print('checkRelation22', name, tName, rList[tName])

    if len(rList[tName]) > 0:
      checkRelation(rList, tName)
    print('?????????', rList, name, tName, len(rList[tName]) > 0)

# RList = {'Fred': ['Barney'], 'Barney': ['Fred', 'Betty'], 'Betty': ['Wilma', 'Barney'], 'Wilma': ['Betty']}

# copyRList = copy.deepcopy(RList)
# checkRelation(copyRList, list(RList.keys())[0])

# result = 0
# for i in copyRList:
#   if(len(copyRList[i]) == 0):
#     result += 1
# print(copyRList, result)

for i in range(F):
  RList = {}
  fCount = int(input())
  for j in range(fCount):
    fRelation = input().rstrip().split(' ')

    if fRelation[0] in RList:
      RList[fRelation[0]].append(fRelation[1])
    else :
      RList[fRelation[0]] = [fRelation[1]]

    if fRelation[1] in RList:
      RList[fRelation[1]].append(fRelation[0])
    else :
      RList[fRelation[1]] = [fRelation[0]]

    print('RList', RList)
    copyRList = copy.deepcopy(RList)
    checkRelation(copyRList, list(RList.keys())[0])

    result = 0
    for i in copyRList:
      if(len(copyRList[i]) == 0):
        result += 1
    
    print('copyRList', copyRList, result)
    resultList.append(result)

for i in resultList:
  print(i)
