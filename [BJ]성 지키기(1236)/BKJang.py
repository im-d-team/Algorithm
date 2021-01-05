from sys import stdin
input = stdin.readline

N, M = map(int, input().split(' '))
castle = []
colCastle = []
rowCount = 0
colCount = 0

for _ in range(N):
  castle.append(list(input().rstrip()))

for i in range(N):
  if 'X' not in castle[i]:
    rowCount += 1

for j in range(M):
  if 'X' not in [castle[i][j] for i in range(N)]:
    colCount += 1

print(max(rowCount, colCount))
