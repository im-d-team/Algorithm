num = int(input())
testWord=""
isGoodWord = False
result = 0

def is_pair(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif ch == stack[-1]:
            stack.pop()
        elif ch != stack[-1]:
            stack.append(ch)


    return len(stack) == 0


for i in range(num):
    testWord = input()
    isGoodWord = is_pair(testWord)

    if isGoodWord is True:
        result += 1

print(result)
