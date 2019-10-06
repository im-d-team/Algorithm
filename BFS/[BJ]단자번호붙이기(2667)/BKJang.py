from sys import stdin
from collections import deque

# 1. 큐 정의
class Queue:
    def __init__(self):
        self.Queue_item = []
        
    # Enqueue 기능 구현
    def enqueue(self,x):
        self.Queue_item.append(x)
        return None
    
    # Dequeue 기능 구현
    def dequeue(self):
        item_length = len(self.Queue_item)
        if item_length < 1:
          return False
        result = self.Queue_item[0]
        del self.Queue_item[0]
        return result
    
    # isEmpty 기능 구현
    def isEmpty(self):
        return not self.Queue_item

queue = Queue()
resultSizeArr = []

# 3. bfs 함수 정의
def bfs(inputArr, i, j, resultPoint, count):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, 1, -1]
  queue.enqueue((i, j, resultPoint))
  inputArr[i][j] = resultPoint
  while(not queue.isEmpty()):
    x, y, point = queue.dequeue()
    for i in range(4):
      if (x + dx[i] >= 0 and x + dx[i] < len(inputArr) and y + dy[i] >= 0 and y + dy[i] < len(inputArr)):
        if (inputArr[x + dx[i]][y + dy[i]] == '1'):
          count = bfs(inputArr, x + dx[i], y + dy[i], point, count + 1)

  return count

# 2. 입력 값 받아 2차원 배열 만들기 
input = stdin.readline
size = int(input())
inputArr = []
resultPoint = -1

for _ in range(size):
  inputArr.append(list(input()))
  length = len(inputArr)
for i in range(length):
    for j in range(length):
      if (inputArr[i][j] == '1'):
        resultSize = bfs(inputArr, i, j, resultPoint, 1)
        resultSizeArr.append(resultSize)
        resultPoint -= 1

print(abs(resultPoint + 1))
resultSizeArr.sort()
for i in resultSizeArr:
  print(i)