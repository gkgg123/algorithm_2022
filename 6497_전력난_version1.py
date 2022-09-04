import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

while True:
    N,M = map(int,input().split())
    if N+M == 0:
        break
    graph = [{} for _ in range(N)]

    total_pay = 0
    for _ in range(M):
        x,y,z = map(int,input().split())
        total_pay += z
        if graph[x].get(y) != None:
            graph[x][y] = min(graph[x][y],z)
            graph[y][x] = min(graph[y][x],z)
        else:
            graph[x][y] = z
            graph[y][x] = z
    INF = float('inf')
    distance = [INF for _ in range(N)]
    distance[0] = 0
    visited = [False for _ in range(N)]
    node_list = []
    heapq.heappush(node_list,(0,0))
    while node_list:
        dis,node = heapq.heappop(node_list)
        if visited[node]:
            continue
        visited[node] = True
        total_pay -= dis
        for next_node in graph[node]:
            if distance[next_node] > graph[node][next_node]:
                distance[next_node] = graph[node][next_node]
                heapq.heappush(node_list,(distance[next_node],next_node))

    print(total_pay)

