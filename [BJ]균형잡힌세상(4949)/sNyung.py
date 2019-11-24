import sys

def checkBracket(bracket):
  return ")" if bracket == "(" else "]"

while True:
  sentence = sys.stdin.readline().rstrip()
  if sentence == ".":
    break
  
  check = True
  stack = []

  for c in sentence:
    if c == '(' or c == '[':
      stack.append(c)
    elif c == ')' or c == ']':
      if len(stack) == 0:
        check = False
        break
      if checkBracket(stack.pop(-1)) == c:
        continue
      else:
        check = False
        break
    
  if check and not stack:
    print('yes')
  else:
    print('no')