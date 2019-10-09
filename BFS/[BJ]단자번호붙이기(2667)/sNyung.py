from sys import stdin
from collections import deque
input = stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def BFS(size, ap):
  cur = []
  apn = 0
  Q = deque()
  Q.append((0, 0, 0))

  while Q:
    x, y, pn = Q.popleft()
    if ap[x][y] == 1 :
      if pn == 0 :
        apn += 1
        cur.append(1)
      else:
        cur[apn-1] += 1

    cn = ap[x][y]
    ap[x][y] = -1

    for mx, my in direction:
      nx, ny = x + mx, y + my
      if nx < 0 or ny < 0 or nx >= size or ny >= size or ap[nx][ny] == -1: continue
      Q.appendleft((nx, ny, cn)) if cn == 1 else Q.append((nx, ny, cn))
      
  print(apn)
  cur.sort()
  for _ in cur:
    print(_)

size = int(input())
ap = [list(map(int, list(input().split()[0]))) for _ in range(size)]

BFS(size, ap)