from sys import stdin
input = stdin.readline

N = int(input())
sum = 0
num = 1
count = 0

while N != sum:
  if sum + num > N:
    num = 1
  else:
    sum += num
    num += 1
    count += 1

print(count)
