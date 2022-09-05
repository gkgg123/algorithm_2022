import sys

def input():
    return sys.stdin.readline().rstrip()


def solve(node):
    cnt = 0
    ex = node
    ey = arr[ex]
    for px in range(node):
        py = arr[px]
        for cx in range(px+1,node):
            cy = arr[cx]
            ccw = (cx-px)*(ey-py) - (cy-py)*(ex-px)
            if ccw <=0:
                break
        else:
            cnt += 1
    

    for px in range(N-1,node,-1):
        py = arr[px]
        for cx in range(px-1,node,-1):
            cy = arr[cx]
            ccw = (cx-px)*(ey-py) - (cy-py)*(ex-px)
            if ccw >=0:
                break
        else:
            cnt +=1
    return cnt

N = int(input())

result = 0

arr = list(map(int,input().split()))
for i in range(N):
    temp_max = solve(i)
    if temp_max> result:
        result = temp_max
print(result)