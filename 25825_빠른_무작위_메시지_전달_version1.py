import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(node,cnt,add):
    global result
    if add>=result:
        return
    if cnt == N:
        result = min(result,add)
        return
    visited[node] = False
    group[node//2] = False
    if cnt%2:
        other = [node//2*2,node//2*2+1]
        for next in other:
            if next == node:
                continue
            solve(next,cnt+1,add + arr[node][next])
    else:
        for num in range(N):
            if visited[num] and group[num//2]:
                solve(num,cnt+1,add + arr[node][num])
    visited[node] = True
    group[node//2] = True
N = 12
arr = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')
result = INF

visited = [True for _ in range(N)]
group = [True for _ in range(N)]


for num in range(N):
    solve(num,1,0)
print(result)