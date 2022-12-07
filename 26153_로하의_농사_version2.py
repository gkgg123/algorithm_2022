import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(x,y,prevD,useK):
    visit.add((x,y))
    temp = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<N and 0<=ny<M:
            if (nx,ny) not in visit:
                if prevD == idx and useK>0:
                    temp = max(temp,solve(nx,ny,prevD,useK-1))
                elif useK>1:
                    temp = max(temp,solve(nx,ny,idx,useK-2))
    visit.remove((x,y))
    return temp + arr[x][y]

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
x,y,k = map(int,input().split())
visit = set()
visit.add((x,y))
result = 0
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and k:

        result = max(result,solve(nx,ny,i,k-1))

print(result +arr[x][y])