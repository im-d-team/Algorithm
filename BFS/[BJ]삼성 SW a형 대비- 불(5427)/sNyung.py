from sys import stdin
from collections import deque

input = stdin.readline

def bfs(width, height, Q, board):
  direction = [(1, 0),(-1, 0),(0, 1),(0, -1)]

  while Q:
    flag, x, y = Q.popleft()
    for i in range(4):
      moveX, moveY = x + direction[i][0], y + direction[i][1]
      if (moveX < 0 or moveY < 0 or moveX >= width or moveY >= height):
        if flag == -1 : continue
        return flag
      if(board[moveX][moveY] == -1):
        continue
      board[moveX][moveY] = -1
      Q.append((-1 if flag == -1 else flag + 1, moveX, moveY))
  return "IMPOSSIBLE"

for _ in range(int(input())):
  x, y = map(int, input().split(" "))
  b = [list(input()) for _ in range(y)]
  Q = deque()
  p = ()
  board = [[0] * x for _ in range(y)] 
  
  for i in range(y):
    for j in range(x):
      if b[i][j] == '.':
        continue
      if b[i][j] == '*':
        Q.append((-1, i, j))
      elif b[i][j] == '@':
        p = (1, i, j)
      board[i][j] = -1

  Q.append(p)
  print(bfs(y, x, Q, board))