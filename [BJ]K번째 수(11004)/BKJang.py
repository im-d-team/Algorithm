from sys import stdin
input = stdin.readline

N, K = map(int, input().split(' '))
inputList = list(map(int, input().split(' ')))

inputList.sort()

print(inputList[K-1])