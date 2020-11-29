from sys import stdin
input = stdin.readline

def binary_search(target, start, end, data):
  if start > end:
    return 0

  mid = (start+end)//2

  if data[mid] == target:
    return 1
  elif data[mid] > target:
    end = mid - 1
  else:
    start = mid + 1

  return binary_search(target, start, end, data)

N = int(input())
NList = sorted(list(map(int, input().split(' '))))
M = int(input())
MList = list(map(int, input().split(' ')))

for num in MList:
  resultList.append(binary_search(num, 0, N - 1, NList))

for num in resultList:
  print(num)
