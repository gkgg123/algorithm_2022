import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


def dijkstra(st,flag):
    node_list = []
    heapq.heappush(node_list,(0,st))
    distance[flag][st] = 0
    while node_list:
        cur_dis, node  = heapq.heappop(node_list)
        if distance[flag][node] < cur_dis:
            continue

        for next_node in graph[flag][node]:
            if distance[flag][next_node] > graph[flag][node][next_node] + cur_dis:
                distance[flag][next_node] = graph[flag][node][next_node] + cur_dis
                heapq.heappush(node_list,(distance[flag][next_node],next_node))
N,M,X = map(int,input().split())
graph = [[{} for _ in range(N+1)] for _ in range(2)]

for _ in range(M):
    a,b,t = map(int,input().split())
    graph[0][a][b] = t
    graph[1][b][a] = t

INF = float('inf')
distance = [[INF for _ in range(N+1)] for _ in range(2)]


dijkstra(X,0)
dijkstra(X,1)
result = 0 

for node in range(1,N+1):
    if node == X:
        continue
    if result < distance[0][node] + distance[1][node]:
        result = distance[0][node] + distance[1][node]

print(result)