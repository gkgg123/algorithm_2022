import sys

def input():
    return sys.stdin.readline().rstrip()


def solve(cx,cy,px,py):
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == arr[cx][cy]:
            if (px,py) == (nx,ny):
                continue
            if visited[nx][ny]:
                print('Yes')
                exit()
            visited[nx][ny] = True
            solve(nx,ny,cx,cy)
             

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
for x in range(N):
    for y in range(M):
        if visited[x][y]:
            continue
        visited[x][y] = True
        solve(x,y,-1,-1)
print('No')
