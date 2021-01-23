from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
start, end = 1, 0

for _ in range(m):
  x, y, weight = map(int, input().split())
  adj[x].append((y, weight))
  adj[y].append((x, weight))

start_node, end_node = map(int, input().split())

def bfs(c):
  queue = deque([start_node])
  visited = [False] * (n + 1)
  visited[start_node] = True
  while queue:
    x = queue.pop()
    for y, weight in adj[x]:
      if not visited[y] and weight >= c:
        visited[y] = True
        queue.append(y)
  
  return visited[end_node]

result = start

for i in adj[end_node]:
  end = max(end, i[1])

while start <= end:
  mid = (start + end) // 2
  if bfs(mid):
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)