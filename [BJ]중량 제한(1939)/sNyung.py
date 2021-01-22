from collections import deque
from sys import stdin
input = stdin.readline

def bfs(x, th):
  q = deque()
  c = [0 for _ in range(N)]
  q.append(x)
  c[x] = 1

  while q:
    x = q.pop()

    for nx, w in a[x]:
      if c[nx] == 0 and w >= th:
        c[nx] = 1
        q.append(nx)

  if c[y-1] == 1:
    return 1
  else:
    return 0

N, M = map(int, input().split())
a = [[] for _ in range(N)]

for _ in range(M):
  x, y, w = map(int, input().split())
  a[x-1].append([y-1, w])
  a[y-1].append([x-1, w])

X, Y = map(int, input().split()) # start, end

left, right = 1, 0

for i in a[Y-1]:
  right = max(right, i[1]) # find MAX

while left <= right:
  mid = (left + right) // 2

  if bfs(X-1, mid):
    ans = mid
    left = mid + 1
  else:
    right = mid - 1

print(ans)
