testCaseCount = int(input())
answerCount = 0
testCaseArr = []
testCaseStrikeBallArr = []

for i in range(testCaseCount):
    inputArr = list(map(int, input().split(' ')))
    numberForCompareArr = list(map(int, list(str(inputArr[0]))))
    testCaseArr.append(numberForCompareArr)
    testCaseStrikeBallArr.append([inputArr[1], inputArr[2]])

for i in range(123, 988):
    sameCount = 0
    check = False
    compareArr = list(map(int, (str(i))))
    if (compareArr[0] == compareArr[1] or compareArr[1] == compareArr[2] or compareArr[0] == compareArr[2]
            or compareArr[0] == 0 or compareArr[1] == 0 or compareArr[2] == 0):
        continue

    for j in range(testCaseCount):
        strike = 0
        ball = 0

        for a in range(0, 3):
            for b in range(0, 3):
                if (testCaseArr[j][a] == compareArr[b]):
                    if (a == b):
                        strike += 1
                    else:
                        ball += 1

        if(strike == testCaseStrikeBallArr[j][0]
           and ball == testCaseStrikeBallArr[j][1]):
            sameCount += 1

    if (sameCount == testCaseCount):
        answerCount += 1

print(answerCount)
