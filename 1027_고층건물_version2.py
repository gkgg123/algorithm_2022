import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int,input().split()))

views = [0 for _ in range(N)]
for x in range(N):
    slopes = -float('inf')
    for y in range(x+1,N):
        cur_slope = (arr[y]-arr[x])/(y-x)
        if cur_slope > slopes:
            slopes = cur_slope
            views[x] += 1
            views[y] += 1
print(max(views))