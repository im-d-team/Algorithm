from sys import stdin
input = stdin.readline

N, r, c = list(map(int, input().split(' ')))

# memo = {
#   (0, 0) : 0,
#   (0, 1) : 1,
#   (1, 0) : 2,
#   (1, 1) : 3,
# }

# @TODO Maximum Recursion
# def get_recursion(row, col):
#   if (row, col) not in memo:
#     if col == 1 or col == 0:
#       value = get_recursion(row - 2, col) + 2 ** N * 2
#     else:
#       value = get_recursion(row, col - 2) + 4
#     memo[(row, col)] = value
#     return value

#   return memo[(row, col)]

# @TODO 메모리초과
# def get_recursion(X, Y):
#   for row in range(2 ** N):
#     for col in range(2 ** N):
#       if (row, col) not in memo:
#         if col == 1 or col == 0:
#           value = memo[(row - 2, col)] + 2 ** N * 2
#         else:
#           value = memo[(row, col - 2)] + 4
#         memo[(row, col)] = value
  
#       if X == row and Y == col:
#         print(memo[(X, Y)])
#         break


# @TODO 시간 초과
# N, X, Y= map(int, input().split())

# result = 0
# def solve(n, x, y):
#     global result
#     if n ==2:
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
        
#         if x==X and y+1 ==Y:
#             print(result)
#             return
#         result += 1
        
#         if x+1 == X and y == Y:
#             print(result)
#             return
#         result += 1
        
#         if x+1 == X and y+1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n/2,x,y)
#     solve(n/2, x, y+n/2)
#     solve(n/2, x+n/2, y)
#     solve(n/2, x+n/2, y+n/2)    
    

# solve(2**N, 0,0)   

def recur(N, r, c, num):

    if N == -1:
        print(num)
        return

    if c < ((2 ** N) / 2):
        if r < ((2 ** N) / 2):
            # print("1사분면")
            pass
        else:
            # print("3사분면")
            num += (2**(2*N - 2) * 2)
            r -= ((2 ** N) // 2)
    else:
        if r < ((2 ** N) // 2):
            # print("2사분면")
            num += (2**(2*N - 2))
            c -= ((2 ** N) // 2)
        else:
            # print("4분면")
            num += (2**(2*N - 2) * 3)
            r -= ((2 ** N) // 2)
            c -= ((2 ** N) // 2)

    recur(N - 1, r, c, num)

recur(N, r, c, 0)
