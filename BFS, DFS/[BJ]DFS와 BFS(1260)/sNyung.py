from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start, movePList):
  q = deque([start])
  b = [start == _ for _ in range(len(movePList))]

  while q:
    n = q.popleft()
    print(n + 1, end=" ")
    for m in movePList[n]:
      if not b[m]:
        b[m] = True
        q.append(m)
  return

def dfs(start, movePList):
  s = [(start, 0)]
  b = [start == _ for _ in range(len(movePList))]
  print(start + 1, end=" ")
  while len(s):
    t = s.pop()
    nn, nt = t[0], t[1]

    checkList = movePList[nn][nt:]
    for m in range(len(checkList)):
      e = checkList[m]
      if not b[e]:
        print(e + 1, end=" ")
        b[e] = True
        s.append((nn, m + 1))
        s.append((e, 0))
        break
  return

t, l, start = map(int, input().split(" "))
movePList = [[] for _ in range(t)]
movePList2 = []

for _ in range(l):
  sp, ep =  map(lambda x: int(x) - 1, input().split(" "))
  movePList[sp].append(ep)
  movePList[ep].append(sp)

for list in movePList:
  movePList2.append(sorted(list))

dfs(start-1, movePList2)
print()
bfs(start-1, movePList2)