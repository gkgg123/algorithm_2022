import queue
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
keyBind = {
    'o' : 0,
    'v' : 1,
}
answer = [0,0]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            visited[x][y] = True
            cnt = [0,0]
            queue = deque()
            queue.append((x,y))
            # v는 늑대 o는 양
            if arr[x][y] == 'v' or arr[x][y] == 'o':
                cnt[keyBind[arr[x][y]]] += 1
            while queue:
                cx,cy = queue.popleft()

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if visited[nx][ny]:
                            continue
                        if arr[nx][ny] != '#':
                            queue.append((nx,ny))
                            visited[nx][ny] = True
                            if arr[nx][ny] == 'v' or arr[nx][ny] == 'o':
                                cnt[keyBind[arr[nx][ny]]] += 1
            if cnt[0] > cnt[1]:
                answer[0] += cnt[0]
            else:
                answer[1] += cnt[1]

print(*answer)

