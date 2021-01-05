from sys import stdin
input = stdin.readline

N = int(input())
titleDict = {}
maxValueList = []

for _ in range(N):
  title = input().rstrip()
  if title not in titleDict:
    titleDict[title] = 1
  else:
    titleDict[title] += 1

allValues = titleDict.values()
maxValue = max(titleDict.values())

for key, value in titleDict.items():
  if value == maxValue:
    maxValueList.append(key)

maxValueList.sort()

print(maxValueList[0])