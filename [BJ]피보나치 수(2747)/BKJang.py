from sys import stdin
input = stdin.readline

param = int(input())

memo = {
  1: 1,
  2: 1
}
def get_fibo(value):
  if value not in memo:
    fibo_value = get_fibo(value - 1) + get_fibo(value -2)
    memo[value] = fibo_value
    return fibo_value
  else:
    return memo[value]

print(get_fibo(param))
