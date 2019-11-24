import sys
read = sys.stdin.readline

n = int(read())
w = [[0] * n for _ in range(n)]

for i in range(n):
    row = read().split()
    for j in range(len(row)):
        w[i][j] = int(row[j])

def tsp():
    global w
    global n
    memo = [[None] * (1 << n) for _ in range(n)]
    INF = 987654321
    
    def isAllVisited(visited):
        return visited == (1 << n) - 1

    def isNotVisited(visited, i):
        return visited & (1 << i) == 0

    def isMe(w, fromCity, toCity):
        return w[fromCity][toCity] != 0
    
    def isMemoed(memo, last, visited):
        return memo[last][visited] is not None
    
    def marking(visited, nextCity):
        return visited | (1 << nextCity)

    def dp(last, visited):
        if isAllVisited(visited):
            return w[last][0] or INF

        if isMemoed(memo, last, visited):
            return memo[last][visited]

        tmp = INF
        for i in range(n):
            if isNotVisited(visited, i) and isMe(w, last, i):
                newVisited = marking(visited, i)
                tmp = min(tmp, dp(i, newVisited) + w[last][i])

        memo[last][visited] = tmp
        return tmp

    return dp(0, 1 << 0)

print(tsp())
