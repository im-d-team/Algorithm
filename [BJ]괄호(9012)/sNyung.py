
from sys import stdin
input = stdin.readline

OPEN = "("
count = int(input())

for count_idx in range(count):
  word = input().rstrip()

  if(word[0] != OPEN):
    print('NO')
  else:
    wordStack = []
    
    for word_al in word:
      if word_al != OPEN:
        if len(wordStack) == 0:
          wordStack.append(OPEN)
          break
        wordStack.pop()
      else:
        wordStack.append(OPEN)
    if len(wordStack) == 0:
      print("YES")
    else:
      print("NO")
