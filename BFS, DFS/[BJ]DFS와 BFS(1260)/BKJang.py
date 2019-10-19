
from sys import stdin
from collections import deque

# 1. 입력 값 받기
input = stdin.readline
n, m, v = map(int, input().split(' '))
# 1-1. 입력 값을 받아 행렬을 만든다.
matrix = [[0] * (n + 1) for _ in range(n + 1)]
# 1-2. 행렬의 이어진 부분들을 1로 바꿔준다.
for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

# 2. dfs 함수
def dfs(current, matrix, visited):
  visited.append(current)
  for i in range(len(matrix[current])):
    if (matrix[current][i] and i not in visited):
      visited = dfs(i, matrix, visited)
  
  return visited

# 3. bfs 함수
def bfs(queue, matrix, current):
  queue.append(current)
  visited = [current]

  while queue:
    now = queue.popleft() 
    for i in range(len(matrix[now])):
      if (matrix[now][i] and i not in visited):
        queue.append(i)
        visited.append(i)

  return visited

queue = deque()
print(*dfs(v, matrix, []))
print(*bfs(queue, matrix, v))
