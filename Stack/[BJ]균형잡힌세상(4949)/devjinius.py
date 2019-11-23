from sys import stdin
from collections import deque
read = stdin.readline

def isEnd(str):
	return str == '.'

def isOpen(c):
	return c == '(' or c == '['

def isClose(c):
	return c == ')' or c == ']'

def validPop(c, stack):
	if not len(stack):
		return False
	if c == ']' and stack[-1] == '[':
		return True
	if c == ')' and stack[-1] == '(':
		return True

	return False

while True:
	str = read().rstrip()
	if isEnd(str):
		break
	
	stack = deque()
	flag = True

	for c in str:
		if isOpen(c):
			stack.append(c)
		elif isClose(c):
			if validPop(c, stack):
				stack.pop()
			else:
				print('no')
				flag = False
				break
	if flag:
		if len(stack):
			print('no')
		else:
			print('yes')
