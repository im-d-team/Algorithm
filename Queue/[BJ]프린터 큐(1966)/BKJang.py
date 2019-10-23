from sys import stdin
from collections import deque
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1
testCase = int(input())
for _ in range(testCase):
  n, m = map(int, input().split(' '))
  inputArr = list(map(int, input().split(' ')))
  priorityArr = [i for i in inputArr]
  indexArr = []
  queue = deque()
  count = 0

  for i in range(n):
    indexArr.append(0)
    queue.append(i)

  while queue:
    current = queue.popleft()

    if (inputArr[current] == max(priorityArr)):
      priorityArr.remove(max(priorityArr))
      indexArr[current] = count
      count += 1
    else:
      queue.append(current)
    
  print(indexArr[m] + 1)
