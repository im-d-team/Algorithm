from sys import stdin
input = stdin.readline

print(''.join(sorted(input().rstrip(), reverse = True)))