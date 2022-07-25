import queue
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def sol():
    queue = deque()

    for num in range(1,K+1):
        if virus[num]:
            queue.extend(virus[num])
    t = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue and t<S:
        len_q = len(queue)
        for _ in range(len_q):
            x,y,num = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if arr[nx][ny]:
                        continue
                    arr[nx][ny] = num
                    if nx == X and ny == Y:
                        return arr[X][Y]
                    queue.append((nx,ny,num))

        t += 1
    return arr[X][Y]
N,K = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]

virus = [[] for _ in range(K+1)]
for x in range(N):
    for y in range(N):
        if arr[x][y]:
            virus[arr[x][y]].append((x,y,arr[x][y]))

S,X,Y = map(int,input().split())
X -= 1;Y -= 1
print(sol())