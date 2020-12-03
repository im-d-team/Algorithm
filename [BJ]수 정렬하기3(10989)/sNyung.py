from sys import stdin
input = stdin.readline

N = int(input())
Nlist = {}

for i in range(N):
  value = int(input())
  if value not in Nlist:
    Nlist[value] = 1
  else:
    Nlist[value] += 1

Nlist = sorted(Nlist.items())

for i in Nlist:
  k, v = i
  for _ in range(v):
    print(k)