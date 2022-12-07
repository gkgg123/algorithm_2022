import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()



def solve(a,b,t,dire):
    if t == 0:
        return 0
    tmp = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if (nx,ny) in visit:
                continue
            visit.add((nx,ny))
            if dire == -1:
                tmp = max(tmp,solve(nx,ny,t,i))
            elif dire%2 == ((i+2)%4)%2:
                tmp = max(tmp,solve(nx,ny,t-1,i))
            elif dire%2 != ((i+2)%4)%2 and t>1:
                tmp = max(tmp,solve(nx,ny,t-2,i))
            visit.remove((nx,ny))
    return tmp + arr[a][b]

N,M = map(int,input().split())


dx = [-1,0,1,0]
dy = [0,-1,0,1]
arr = [list(map(int,input().split())) for _ in range(N)]

x,y,k = map(int,input().split())
visit = set()
visit.add((x,y))
if k:
    print(solve(x,y,k,-1))
else:
    print(arr[x][y])