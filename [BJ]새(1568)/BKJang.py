from sys import stdin
input = stdin.readline

N = int(input())
current = 1
count = 0

while N > 0:
  if N < current:
    current = 1
  else:
    N -= current
    current += 1
    count += 1

print(count)