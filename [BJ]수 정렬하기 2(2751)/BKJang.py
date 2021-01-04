from sys import stdin
input = stdin.readline

count = int(input())
inputList = []

for _ in range(count):
  inputList.append(int(input().rstrip()))

inputList.sort()

for i in inputList:
  print(i)