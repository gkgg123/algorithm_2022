import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def solve(r1,c1,r2,c2):
    queue = deque()
    queue.append((r1,c1,0))
    if r1 == r2 and c1 == c2:
        return 0
    visit = set()
    visit.add((r1,c1))
    dx = [-2,-2,0,0,2,2]
    dy = [-1,1,-2,2,-1,1]
    while queue:
        cx,cy,cnt = queue.popleft()

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny) not in visit:
                    visit.add((nx,ny))
                    if nx == r2 and ny == c2:
                        return cnt + 1
                    queue.append((nx,ny,cnt+1))

    return -1

N = int(input())

r1,c1,r2,c2 = map(int,input().split())

print(solve(r1,c1,r2,c2))