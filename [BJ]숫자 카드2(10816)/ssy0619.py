#10
#6 3 2 10 10 10 -10 -10 7 3
#8
#10 9 -5 2 3 4 5 -10

n = int(input())
nList = list(map(int, input().split(' ')))
m = int(input())
mLlist = list(map(int, input().split(' ')))

count = {}

for n in nList:
    try:
        count[n] += 1
    except:
        count[n] = 1

result = []

for m in mLlist:
    try:
        result.append((count[m]))
    except:
        result.append(0)

for i in result:
    print(i, end = ' ')
