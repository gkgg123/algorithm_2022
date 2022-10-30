import sys

def input():
    return sys.stdin.readline().rstrip()

#  왼쪽, 왼쪽위 위쪽 애벌레 크기만큼
N, M = map(int,input().split())


arr = [[1 for _ in range(N)] for _ in range(N)]

prefix_sum = [0 for _ in range(N*2+1)]
for _ in range(M):
    x,y,z = list(map(int,input().split()))
    if y:
        prefix_sum[x] += 1
        prefix_sum[x+y] -= 1
    if z:
        prefix_sum[x+y] += 2

for i in range(1,2*N):
    prefix_sum[i] += prefix_sum[i-1]

idx = 0
x,y = N-1,0
dx,dy = -1,0
while idx<2*N-1:
    arr[x][y] += prefix_sum[idx]
    nx,ny = x +dx, y + dy
    if 0<=nx<N and 0<=ny<N:
        x,y = nx,ny
    else:
        dx,dy = 0,1
        x,y = x +dx, y + dy
    idx += 1

for x in range(N):
    for y in range(N):
        if x == 0 or y == 0:
            continue
        arr[x][y] = arr[x-1][y]

for row in arr:
    print(*row)