from sys import stdin
from collections import deque

read = stdin.readline

n = int(read())

matrix = [[-1] * (n+2) for _ in range(n+2)]
visited = [[0] * (n+2) for _ in range(n+2)]

for i in range(n):
    row = list(map(int, read().rstrip()))
    for j in range(n):
        matrix[i+1][j+1] = row[j]

def bfs():
    (i, j) = q.popleft()
    if visited[i][j]:
        return

    global count
    count += 1
    visited[i][j] = 1
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if matrix[ni][nj] == -1 or matrix[ni][nj] == 0:
            continue
        if visited[ni][nj]:
            continue
        q.append((ni, nj))

q = deque()
village = []
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)
global count
    
for i in range(n+2):
    for j in range(n+2):
        if visited[i][j]:
            continue
        if matrix[i][j] == 1:
            count = 0
            q.append((i, j))
            while q:
                bfs()
            village.append(count)
        
print(len(village))
for i in sorted(village):
    print(i)