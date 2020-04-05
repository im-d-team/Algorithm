# 3
# ABAB
# AABB
# ABBA

from sys import stdin
input = stdin.readline

count = int(input())
resultCount = 0
testCaseArr = []
for _ in range(count):
  testCaseArr.append(input())


for testCase in testCaseArr:
  stack = []
  # 1. 각각의 input을 받는다.
  inputArr = list(testCase.rstrip())
  # 2. inputArr loop
  for i in range(len(inputArr)):
    current = inputArr[i]
    # 3-1. stack의 마지막 값이 현재 inputArr의 value와 같으면 pop
    if len(stack) and stack[-1] == current:
      stack.pop()
    # 3-2. stack의 마지막 값이 현재 inputArr의 value와 다르거나 비어있으면 append
    elif len(stack) == 0 or stack[-1] != current:
      stack.append(current)

  if len(stack) == 0:
    resultCount += 1

print(resultCount)