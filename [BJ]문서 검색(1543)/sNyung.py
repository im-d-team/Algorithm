from sys import stdin
input = stdin.readline

total = input().rstrip()
word = input().rstrip()

count = 0
i = 0

while i <= len(total) - len(word):
  if total[i : i + len(word)] == word:
    count += 1
    i += len(word)
  else:
    i += 1

print(count)