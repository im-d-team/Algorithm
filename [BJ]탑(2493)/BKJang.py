# 5
# 6 9 5 7 4
# 0 0 2 2 4

from sys import stdin
input = stdin.readline

count = int(input())
inputArr = list(map(int, input().split(' ')))
stack = []
result = [0 for i in range(count)]

for i in range(count):
    while len(stack):
        if stack[-1][1] > inputArr[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, inputArr[i]))

print(' '.join(list(map(str, result))))
