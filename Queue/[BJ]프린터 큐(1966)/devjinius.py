import sys
read = sys.stdin.readline

testLen = int(read())

for _ in range(testLen):
    n, m = map(int, read().split(" "))
    printQueue = list(map(int, read().split(" ")))
    priQueue = sorted(printQueue, reverse=True)
    count = 0

    while 1:
        if (m == 0):
            if priQueue[0] == printQueue[0]:
                count += 1
                print(count)
                break
            else:
                printQueue.append(printQueue.pop(0))
                m = len(priQueue)-1
                continue

        if priQueue[0] == printQueue[0]:
            printQueue.pop(0)
            priQueue.pop(0)
            count += 1
        else:
            printQueue.append(printQueue.pop(0))

        m -= 1