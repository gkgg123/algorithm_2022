import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(total,mid,N):
    left = (total-mid)//2
    if  N <= left:
        return solve(left,mid-1,N)
    elif N> left+mid:
        return solve(left,mid-1,N-left-mid)
    elif N-left-1:
        return 'o'
    return 'm'

N = int(input())

total,last = 3,0

while N>total:
    last += 1
    total = total*2 + last + 3

mid = last + 3
print(solve(total,mid,N))