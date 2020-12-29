from sys import stdin
input = stdin.readline

N, K = map(int, input().split(' '))
Nlist = list(map(int, input().split(' ')))

Nlist.sort()

print(Nlist[K - 1])
