from sys import stdin
input = stdin.readline

count = int(input())
inputArr = []

for i in range(count):
  k, v = input().split(' ')
  inputArr.append((int(k), v))

sortedArr = sorted(inputArr, key=lambda input: input[0])

for j in sortedArr:
  k, v = j
  print(k, v.rstrip())