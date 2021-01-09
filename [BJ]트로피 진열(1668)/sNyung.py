from sys import stdin
input = stdin.readline

N = int(input())
inputList = []

for _ in range(N):
  inputList.append(int(input()))

leftMax = 0
leftCount = 0

for i in inputList:
  if i > leftMax:
    leftCount += 1
    leftMax = i

rightMax = 0
rightCount = 0
inputList.reverse()

for j in inputList:
  if j > rightMax:
    rightCount += 1
    rightMax = j
  elif leftMax == rightMax:
    break

print(leftCount)
print(rightCount)
