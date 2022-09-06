import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(N)]
    INF = float('inf')
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = arr[0][0]
    node_list = []
    heapq.heappush(node_list,(arr[0][0],0,0))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while node_list:
        cur,x,y = heapq.heappop(node_list)
        if distance[x][y] <cur:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                next_ = cur + arr[nx][ny]
                if distance[nx][ny] > next_:
                    distance[nx][ny] = next_
                    heapq.heappush(node_list,(distance[nx][ny],nx,ny))

    print(f'Problem {cnt}: {distance[N-1][N-1]}')
    cnt += 1