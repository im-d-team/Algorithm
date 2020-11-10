from sys import stdin
input = stdin.readline

target = list(map(lambda x: int(x), input().split(' ')))
cardList = list(map(lambda x: int(x), input().split(' ')))

targetNum = target[1]
cardLen = len(cardList)

result = 0

for target_one in range(0, cardLen):
  for target_two in range(target_one + 1, cardLen):
    for target_three in range(target_two + 1, cardLen):
      sum = cardList[target_one] + cardList[target_two] + cardList[target_three]
      if targetNum >= sum and result < sum:
        result = sum

print(result)