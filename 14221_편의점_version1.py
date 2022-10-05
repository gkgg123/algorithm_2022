import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def solve():
    INF = float('inf')
    distance = [INF for _ in range(N+1)]
    node_list = []
    for st in store:
        distance[st] = 0
        node_list.append((0,st))
    heapq.heapify(node_list)
    result = 0
    min_dis = INF
    while node_list:
        cur_dis, node = heapq.heappop(node_list)
        if distance[node]<cur_dis:
            continue
        for next_node in graph[node]:
            if distance[next_node] > graph[node][next_node] + cur_dis:
                distance[next_node] = graph[node][next_node] + cur_dis
                heapq.heappush(node_list,(distance[next_node],next_node))
    house.sort()
    for h in house:
        if min_dis > distance[h]:
            min_dis = distance[h]
            result = h
    return result
N,M = map(int,input().split())
graph = [{} for _ in range(N+1)]
for _ in range(M):
    x,y,d = map(int,input().split())
    graph[x][y] = d
    graph[y][x] = d


p,q = map(int,input().split())

house = list(map(int,input().split()))
store = list(map(int,input().split()))

print(solve())