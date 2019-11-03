import sys
read = sys.stdin.readline

num = int(read())

if num != 1:

    a = [0] * (num+1)
    dp = [0] * (num+1)

    for i in range(1, num+1):
        a[i] = int(read())

    dp[1] = a[1]
    dp[2] = a[1] + a[2]

    for i in range(3, num+1):
        dp[i] = max(dp[i-2], dp[i-3] + a[i-1]) + a[i]

    print(dp[num])

else:
    print(read())