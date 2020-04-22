def isVPS(str):
    mylist = []
    for i in str:
        if i == '(':
            mylist.append(i)
        elif i == ')':
            if not mylist:
                return "NO"
            else:
                mylist.pop()
    if not mylist:
        return "YES"
    else:
        return "NO"

num = int(input())
res = []
for i in range(num):
    temp = input()
    res.append(isVPS(temp))
for i in res:
    print(i)
