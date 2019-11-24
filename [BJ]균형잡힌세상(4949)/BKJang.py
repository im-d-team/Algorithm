# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

while True:
  inputString = input()
  stack = []
  answer = True
  
  if (inputString == '.'):
    break

  for word in inputString:
    # 1. 만약 (, [를 만나면 스택에 집어넣는다.
    if (word == '(' or word == '['):
      stack.append(word)
    # 2. 만약 ), ]를 만나면 스택에서 빼서 짝이 맞는지 검증한다.
    if (word == ')' or word == ']'):
      if (not stack):
        answer = False
        break
      if ((word == ')' and stack[-1] != '(') or (word == ']' and stack[-1] != '[')):
        answer = False
        break
      if ((word == ')' and stack[-1] == '(') or (word == ']' and stack[-1] == '[')):
        current = stack.pop()


  if (answer and not stack):
    print('yes')
  else:
    print('no') 