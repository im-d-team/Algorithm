from sys import stdin
input = stdin.readline

N = int(input())
Nlist = list(map(lambda x: int(input().rstrip()), range(N)))

Nlist.sort()

for j in Nlist:
  print(j)
