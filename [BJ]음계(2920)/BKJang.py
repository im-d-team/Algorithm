from sys import stdin
input = stdin.readline

inputList = list(map(lambda i: int(i), input().split(' ')))

result = 'ascending'
for i in range(len(inputList) - 1):
  if inputList[i] + 1 == inputList[i + 1]:
    result = 'ascending'
  elif inputList[i] - 1 == inputList[i + 1]:
    result = 'descending'
  else:
    result = 'mixed'
    break

print(result)
