from sys import stdin
input = stdin.readline

inputArr = list(map(int, input().rstrip()))

stortedArr = sorted(inputArr, key=lambda key: key, reverse=True)

print(''.join(list(map(str, stortedArr))))