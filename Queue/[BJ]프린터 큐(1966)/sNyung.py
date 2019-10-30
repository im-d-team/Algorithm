ts = int(input())

for _ in range(ts):
  # Input length, index
  n, m = map(int, input().split(" "))
  weightList = list(map(int, input().split(" ")))
  outIndex = 0
  result = 0

  # Create Tuple List (value, m?)
  q = [(x, True if i == m else False) for i, x in enumerate(weightList)]

  while q:
    maxValue = max(q)
    firstElement = q.pop(0)

    if maxValue[0] == firstElement[0]:
      outIndex += 1
      if firstElement[1]:
        result = outIndex
        break
    else:
      q.append(firstElement)
    
  print(result)