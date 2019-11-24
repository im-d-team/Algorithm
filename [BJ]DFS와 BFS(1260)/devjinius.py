import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit = 100000

def dfs(num):
    if visited[num]:
        return
    
    visited[num] = 1
    result.append(num)

    for i in range(1, n+1):
        if matrix[num][i] and not visited[i]:
            dfs(i)

def bfs():
    while q:
        num = q.popleft()
        
        if visited[num]:
            continue
        
        visited[num] = 1      
        result.append(num)

        for i in range(1, n+1):
            if matrix[num][i] and not visited[i]:
                q.append(i)

n, m, v = map(int, input().split(" "))

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split(" "))
    matrix[a][b] = 1
    matrix[b][a] = 1

visited = [0]*(n+1)
result = deque()

dfs(v)
print(" ".join(map(str, result)))

for i in range(1, n+1):
    visited[i] = 0
result = deque()
q = deque()

q.append(v)

bfs()
print(" ".join(map(str, result)))