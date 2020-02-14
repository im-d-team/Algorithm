from sys import stdin
input = stdin.readline

count = int(input())
inputArr = input().split(' ')
result = [0 for i in range(count)]

for index in range(len(inputArr)):
    left = int(inputArr[index])

    for i in range(len(result)):
        if left == 0 and result[i] == 0:
            result[i] = index + 1
            break

        if result[i] == 0:
            left = left - 1


for resultItem in result:
    print(resultItem, end=' ')
