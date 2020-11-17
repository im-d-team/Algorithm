from sys import stdin
input = stdin.readline

[n, m] = list(map(lambda i: int(i), input().split(' ')))
inputList = list(map(lambda i: int(i), input().split(' ')))

result = 0

for i in range(n):
  for j in range(n):
    for z in range(n):
      sum = inputList[i] + inputList[j] + inputList[z]
      diffFlag = inputList[i] != inputList[j] and inputList[j] != inputList[z] and inputList[i] != inputList[z]
      if sum <= m and sum > result and diffFlag:
        result = sum

print(result)
