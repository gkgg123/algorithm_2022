import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def dijkstra(st,ed):
    node_list = []
    heapq.heappush(node_list,(0,st))
    while node_list:
        cur_dis, node = heapq.heappop(node_list)
        if distance[st][node] < cur_dis:
            continue
        if st != ed and  node == ed:
            return distance[st][ed] + distance[ed][st]
        for next_node in graph[node]:
            if distance[st][next_node] > graph[node][next_node] + cur_dis:
                distance[st][next_node] = graph[node][next_node] + cur_dis
                heapq.heappush(node_list,(distance[st][next_node], next_node))
N,M,X = map(int,input().split())
INF = float('inf')
graph = [{} for _ in range(N+1)]
distance = [[INF if i != j else 0 for i in range(N+1)] for j in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a][b] = t

dijkstra(X,X)
result = 0
for node in range(1,N+1):
    if node == X:
        continue
    result = max(result, dijkstra(node,X))

print(result)