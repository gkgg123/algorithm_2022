import sys

def input():
    return sys.stdin.readline().rstrip()

A = list(input())
B = input()
N = len(B)

stack = []
for val in A:
    stack.append(val)
    if stack[-1] == B[-1] and len(stack)>=N:
        if ''.join(stack[-N:]) == B:
            for _ in range(N):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
        