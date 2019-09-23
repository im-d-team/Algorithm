# 불

## 접근방법

처음 문제를 읽었을 때 불이 퍼져나가는 것을 보고 queue를 사용하는 bfs로 접근했다. 

개인적으로 bfs로 접근할 때 특정 조건의 depth or step을 구해야하는 문제에서는 이 depth를 어떻게 처리해야할지 먼저 고민하는 편이다.
이 문제의 경우 몇 초가 depth가 되었다.

매 tick마다 depth를 같이 계산하여 한꺼번에 처리할 수 있는 경우는 그렇게 처리한다.
안되는 경우 queue에 depth를 같이 저장하여 처리하는 편이다.

전자가 코드가 간결하고 성능도 우수한 편이어서 전자를 우선적으로 고려한다. 이 문제도 전자가 가능했다.

이 문제를 접근할 때 키 포인트는 다음과 같았다.

- depth만을 기록하는 2차원 배열을 따로 만든다.
- 불과 사람을 동일한 로직을 이용하되 flag를 주어 구분한다.

## 코드

```python
from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
	q.append((startX, startY, 0))
	bDepth[startX][startY] = 1
	while q:
		x, y, flag = q.popleft()
		for i in range(4):
			newX, newY = x+dx[i], y+dy[i]
			if newX < 0 or newY < 0 or newX >= h  or newY >= w: # 밖으로 나감
				if flag is 1: continue # 불이면 무시
				print(bDepth[x][y]) # 탈출성공
				return
			if bDepth[newX][newY] or b[newX][newY] == '#': # 이동할 위치가 이미 불이거나 벽이면
				continue
			bDepth[newX][newY] = bDepth[x][y] + 1
			q.append((newX, newY, flag))
	print("IMPOSSIBLE")

for _ in range(int(input())):
    w, h = map(int, input().split(" "))
    b = [list(input()) for _ in range(h)]
    bDepth = [[0]*w for _ in range(h)]
    q = deque()
    startX, startY = 0, 0
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

	# depth 초기화
    for i in range(h):
        for j in range(w):
            if b[i][j] == '*':
                q.append((i, j, 1))
                bDepth[i][j] = 1
            elif b[i][j] == '@':
                startX, startY = i, j
                b[i][j] = '.'
            else:
                bDepth[i][j] = 0

    bfs()
```