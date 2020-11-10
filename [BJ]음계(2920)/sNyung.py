from sys import stdin
input = stdin.readline

listInt = list(map(lambda x: int(x), input().split(' ')))
resultList = {
    -1: 0,
    0: 0,
    1: 0
}

for item in range(len(listInt) - 1):
  curNum = listInt[item]
  nextNum = listInt[item + 1]

  diffNum = nextNum - curNum

  if diffNum > 0:
    resultList[1] += 1
  elif diffNum < 0:
    resultList[-1] += 1
  else:
    resultList[0] += 1
  pass

if resultList[0] == 0 and resultList[1] == 0:
  print('descending')
elif resultList[0] == 0 and resultList[-1] == 0:
  print('ascending')
else:
  print('mixed')
