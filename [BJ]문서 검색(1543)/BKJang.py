from sys import stdin
input = stdin.readline

doc = input().rstrip()
word = input().rstrip()

count = 0
i = 0

while i <= len(doc) - len(word):
  if doc[i : i + len(word)] == word:
    count += 1
    i += len(word)
  else:
    i += 1

print(count)