n = int(input())
inputList = [0] + [int(input()) for _ in range(n)]
maxList = [0] * (n+1)                                                                      
maxList[1] = inputList[1]

if n >= 2:
  maxList[2] = inputList[1]+inputList[2]
  for i in range(3,n+1):
    maxList[i] = max(maxList[i-2]+inputList[i], maxList[i-3]+inputList[i]+inputList[i-1])

print(maxList[n])