import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [list(input()) for _ in range(N)]
INF = float('inf')
visited = [[INF for _ in range(N)] for _ in range(N)]

visited[0][0] = 0

queue = deque()
queue.append((0,0,0))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while queue:
    x,y,cnt = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] <= cnt:
                continue
            if arr[nx][ny] == '1':
                visited[nx][ny] = cnt
                queue.append((nx,ny,cnt))
            elif arr[nx][ny] == '0':
                visited[nx][ny] = cnt+1
                queue.append((nx,ny,cnt+1))


print(visited[N-1][N-1])