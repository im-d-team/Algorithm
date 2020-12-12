# from sys import stdin
# input = stdin.readline

# N, r, c = list(map(int, input().rstrip().split(' ')))
# cnt = 0

# def recur(size, x, y):
#   global cnt
#   if size <= 2:
#     cnt += 1
#     if x == r and y == c:
#       print(cnt)
#       return
#     cnt += 1
#     if x == r and y + 1 == c:
#       print(cnt)
#       return
#     cnt += 1
#     if x + 1 == r and y + 1 == c:
#       print(cnt)
#       return
#     cnt += 1
#     if x + 1 == r and y + 1 == c:
#       print(cnt)
#       return
#   else :
#     recur(size // 2, x, y)
#     recur(size // 2, x, y + size // 2)
#     recur(size // 2, x + size // 2, y)
#     recur(size // 2, x + size // 2, y + size // 2)

# recur(2 ** N, 0, 0)

from sys import stdin
input = stdin.readline

n, r, c = map(int, input().split())
answer = 0

while n >= 1:
  temp = 2 ** (n - 1)

  if n == 1:
    if r == 0 and c == 1:  # 2사분면
      answer += 1
    elif r == 1 and c == 0:  # 3사분면
      answer += 2
    elif r == 1 and c == 1:  # 4사분면
      answer += 3
    break

  if r < temp <= c:  # 2사분면
    answer += temp ** 2
    c -= temp
  elif c < temp <= r:  # 3사분면
    answer += (temp ** 2) * 2
    r -= temp
  elif temp <= r and temp <= c:  # 4사분면
    answer += (temp ** 2) * 3
    r -= temp
    c -= temp

  n -= 1
print(answer)