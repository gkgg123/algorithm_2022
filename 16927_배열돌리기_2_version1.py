import sys

def input():
    return sys.stdin.readline().rstrip()


N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


visited = [[True for _ in range(M)] for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
rotate = []
for k in range(min(N,M)//2):
    temp = []
    cx,cy = k,k
    d = 0

    while visited[cx][cy]:
        visited[cx][cy] = False
        temp.append(arr[cx][cy])
        nx,ny = cx + dx[d], cy + dy[d]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]:
            cx,cy = nx,ny
        else:
            d = d+1
            if d == 4:
                break
            cx,cy = cx + dx[d], cy + dy[d]
    rotate.append(temp[:])

for k in range(min(N,M)//2):
    cx,cy = k,k
    d = 0
    mm = len(rotate[k])
    move = R%mm
    while not visited[cx][cy]:
        visited[cx][cy] = True
        result[cx][cy] = rotate[k][move]
        nx,ny = cx + dx[d], cy + dy[d]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            cx,cy = nx,ny
        else:
            d = d+1
            if d == 4:
                break
            cx,cy = cx + dx[d], cy + dy[d]
        move = (move +1)%mm
for row in result:
    print(*row)
