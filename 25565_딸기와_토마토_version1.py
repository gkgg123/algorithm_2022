import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

def solve():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    used = set()
    counter = []
    for x in range(N):
        for y in range(M):
            if arr[x][y] and (x,y) not in used:
                for i in range(4):
                    cx,cy = x,y
                    temp = [(cx,cy)]
                    cnt = 1
                    while True:
                        nx,ny = cx+dx[i],cy + dy[i]
                        if cnt == K:
                            break
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny]:
                            temp.append((nx,ny))
                            cnt += 1
                            cx,cy = nx,ny
                        else:
                            break
                    if cnt == K:
                        for xx,yy in temp:
                            if (xx,yy) in used:
                                counter.append((xx,yy))
                        used.update(temp)

    ttCnt = 2*K - len(used)
    print(ttCnt)
    if ttCnt:
        if ttCnt == K:
            counter = list(used)
        counter.sort()
        for x,y in counter:
            print(x+1,y+1)
    







N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
total = set()
solve()
