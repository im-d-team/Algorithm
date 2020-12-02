from sys import stdin
input = stdin.readline

N = int(input())
Nlist = []

for i in range(N):
  idx, name = input().rstrip().split(' ')
  Nlist.append((int(idx), name))

Nlist = sorted(Nlist, key=lambda input: input[0])

for i in Nlist:
  print(i[0], i[1])