import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    sys.stdout.write(str(x+y)+'\n')