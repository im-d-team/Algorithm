from sys import stdin
input = stdin.readline

count = int(input())
inputDict = {}

for i in range(count):
  element = int(input())
  if element not in inputDict:
    inputDict[element] = 1
  else:
    inputDict[element] += 1

for j in sorted(inputDict.items()):
  k, v = j
  for _ in range(v):
    print(k)
