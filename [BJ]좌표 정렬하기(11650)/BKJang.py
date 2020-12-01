from sys import stdin
input = stdin.readline

count = int(input())
inputArr = []

for i in range(count):
  k, v = input().split(' ')
  inputArr.append((int(k), int(v)))

sortedArr = sorted(inputArr, key=lambda input: (input[0], input[1]))

for j in sortedArr:
  k, v = j
  print(k, v)