import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort()

for x,y in arr:
    print(x,y)