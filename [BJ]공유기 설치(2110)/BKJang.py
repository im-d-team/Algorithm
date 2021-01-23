from sys import stdin
input = stdin.readline

N, C= map(int, input().split(' '))
NList = list(map(lambda x: int(input()), range(N)))

sortedNList = sorted(NList)
# 1, 2, 4, 8, 9

start = 1
end = sortedNList[-1] - sortedNList[0]
result = 0

while start <= end:
  mid = (start + end) // 2
  value = sortedNList[0]
  count = 1

  for i in range(1, len(sortedNList)):
    if sortedNList[i] >= value + mid:
      value = sortedNList[i]
      count += 1
  if count >= C:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)
