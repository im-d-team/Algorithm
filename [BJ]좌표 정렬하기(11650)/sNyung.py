from sys import stdin
input = stdin.readline

N = int(input())
Nlist = []

for i in range(N):
  idx, name = input().rstrip().split(' ')
  Nlist.append((int(idx), int(name)))

Nlist = sorted(Nlist, key=lambda input: (input[0], input[1]))

for tu in Nlist:
  f, s = tu
  print(f, s)