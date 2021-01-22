import math
from sys import stdin
input = stdin.readline

N, C = map(int, input().split(' '))  # 집 수, 공유기 수
NList = list(map(lambda x: int(input()), range(N)))  # 집의 위치

NList = sorted(NList)

L = 1
R = NList[len(NList) - 1] - NList[0]

result = 0

while(L <= R):
  mid = math.ceil((L + R) / 2)
  cnt = 1
  start = NList[0]

  for n in NList:
    if n - start >= mid:
      cnt += 1
      start = n

  if (cnt >= C):
    result = mid
    L = mid + 1
  else:
    R = mid - 1

print(result)