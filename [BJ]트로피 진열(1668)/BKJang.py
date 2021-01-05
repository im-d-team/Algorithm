from sys import stdin
input = stdin.readline

N = int(input())
inputList = []
max = 0
countLeft = 0
countRight = 0

for _ in range(N):
  inputList.append(int(input()))

for i in inputList:
  if i > max:
    countLeft += 1
    max = i

max = 0
inputList.reverse()

for j in inputList:
  if j > max:
    countRight += 1
    max = j

print(countLeft)
print(countRight)