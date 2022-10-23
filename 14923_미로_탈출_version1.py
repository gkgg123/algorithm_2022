import queue
import sys
from collections import deque
def minus(x):
    return x-1
def input():
    return sys.stdin.readline().rstrip()

def bfs(x,y):
    st = [[INF for _ in range(M)] for _ in range(N)]
    st[x][y] = 0

    queue = deque()
    queue.append((x,y,0))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue:
        cx,cy,cnt = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if st[nx][ny] != INF:
                    continue
                st[nx][ny] = cnt+1
                if not arr[nx][ny]:
                    queue.append((nx,ny,cnt+1))
    return st



N,M = map(int,input().split())


sx,sy = map(minus,map(int,input().split()))

ex,ey = map(minus,map(int,input().split()))
INF = float('inf')

arr = [list(map(int,input().split())) for _ in range(N)]
front = bfs(sx,sy)
back = bfs(ex,ey)

result = front[ex][ey]

for x in range(N):
    for y in range(M):
        if arr[x][y]:
            result = min(result,front[x][y] + back[x][y])

print(-1 if result == INF else result)