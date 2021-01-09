from sys import stdin
input = stdin.readline

N = int(input())
dic = {}

for _ in range(N):
  name = input().rstrip()
  if name not in dic:
    dic[name] = 1
  else:
    dic[name] += 1

maxValue = max(dic.values())
keyList = []

for key, value in dic.items():
  if value == maxValue:
    keyList.append(key)

print(sorted(keyList)[0])