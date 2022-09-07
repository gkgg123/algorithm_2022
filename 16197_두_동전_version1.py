import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def solve():

    while coins:
        x1,y1,x2,y2,cnt = coins.popleft()
        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0<=nx1<N and 0<=nx2<N and 0<=ny1<M and 0<=ny2<M:
                if arr[nx1][ny1] == '#':
                    nx1 = x1
                    ny1 = y1
                if arr[nx2][ny2] == '#':
                    nx2 = x2
                    ny2 = y2
                if not visited[nx1][ny1][nx2][ny2]:
                    coins.append((nx1,ny1,nx2,ny2,cnt+1))
                    visited[nx1][ny1][nx2][ny2] = True
            elif 0<=nx1<N and 0<=ny1<M:
                return cnt + 1
            elif 0<=nx2<N and 0<=ny2<M:
                return cnt +1
    return -1
            
N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

coins = deque()
st = []
for x in range(N):
    for y in range(M):
        if arr[x][y] == 'o':
            arr[x][y] = '.'
            st.append((x,y))
dx = [-1,0,1,0]
dy = [0,-1,0,1]

coins.append((*st[0],*st[1],0))

visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

visited[st[0][0]][st[0][1]][st[1][0]][st[1][1]] = True

print(solve())


