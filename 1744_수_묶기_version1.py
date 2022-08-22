import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def custumpop(fl):
    if fl<0:
        return arr.popleft()
    return arr.pop()

def solve(idx1,idx2,val,fl):
    result = 0
    while arr:
        if len(arr)>=2 and fl*arr[idx1]>=val and fl*arr[idx2]>=val:
            x,y = custumpop(fl), custumpop(fl)
            result += x*y
        else:
            break
    return result

N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()
arr = deque(arr)
result = solve(0,1,0,-1) + solve(-1,-2,2,1)
print(result + sum(arr))
    