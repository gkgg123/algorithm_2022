import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [list(map(int,list(input()))) for _ in range(N)]

node_list = []

heapq.heappush(node_list,(0,0,0))
INF = float('inf')
visited = [[INF for _ in range(N)] for _ in range(N)]

visited[0][0] = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while node_list:
    cnt,x,y = heapq.heappop(node_list)
    if visited[x][y] <cnt:
        continue
    if x == N-1 and y == N-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N:
            next_dist = cnt + (arr[nx][ny]+1)%2
            if visited[nx][ny] > next_dist:
                visited[nx][ny] = next_dist
                heapq.heappush(node_list,(next_dist,nx,ny))



print(visited[N-1][N-1])

