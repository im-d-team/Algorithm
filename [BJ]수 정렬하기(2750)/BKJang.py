from sys import stdin
input = stdin.readline

count = int(input())
inputArr = []

for i in range(count):
  inputArr.append(int(input()))

  inputArr.sort()

for j in inputArr:
  print(j)
