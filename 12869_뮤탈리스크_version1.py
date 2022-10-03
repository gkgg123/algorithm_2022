import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()

def max_zero(a,da):
    return max(a-da,0)
def solve(x,y,z):
    if visited[x][y][z] != INF:
        return visited[x][y][z]
    for dx,dy,dz in permutations([9,3,1]):
        nx = max_zero(x,dx)
        ny = max_zero(y,dy)
        nz = max_zero(z,dz)
        visited[x][y][z] = min(visited[x][y][z],solve(nx,ny,nz)+1)
    return visited[x][y][z]
N = int(input())

arr = list(map(int,input().split())) +[0]*(3-N)
INF = float('inf')
visited = [[[INF for _ in range(61)] for _ in range(61)] for _ in range(61)]
visited[0][0][0] = 0
print(solve(*arr))