from sys import stdin
input = stdin.readline

count = int(input())
result = 0

for count_idx in range(count):
  word = input().rstrip()
  wordStack = [word[0]]

  for word_al in word[1:]: 
    if len(wordStack) > 0 and wordStack[len(wordStack) - 1] == word_al:
      wordStack.pop()
    else:
      wordStack.append(word_al)
  
  if len(wordStack) == 0:
    result += 1

print(result)