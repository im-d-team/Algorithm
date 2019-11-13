# Rn = max(Pi + Rn-i)
from sys import stdin

# 6
# 10
# 20
# 15
# 25
# 10
# 20
input = stdin.readline
testCase = int(input())
inputArr = []
scoreArr = []

for _ in range(testCase):
  inputArr.append(int(input()))

scoreArr.append(inputArr[0])
scoreArr.append(scoreArr[0] + inputArr[1])
scoreArr.append(max(inputArr[1] + inputArr[2], inputArr[0] + inputArr[2]))

for i in range(3, testCase):
  scoreArr.append(max(inputArr[i] + scoreArr[i - 2], inputArr[i] + inputArr[i - 1] + scoreArr[i - 3]))

print(scoreArr[testCase - 1])