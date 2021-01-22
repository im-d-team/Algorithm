from sys import stdin
input = stdin.readline

N, M = map(int, input().split(' '))
board = []
colCastle = []
rowCount = 0
colCount = 0

for _ in range(N):
  row = list(input().rstrip())
  if "X" not in row: 
    rowCount += 1
  board.append(row)

for j in range(M):
  if 'X' not in [board[i][j] for i in range(N)]:
    colCount += 1

print(max(rowCount, colCount))
