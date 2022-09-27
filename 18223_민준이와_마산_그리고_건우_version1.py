import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def solve():
    stack = [N]

    while stack:
        node = stack.pop()
        for prev_node in graph[node]:
            if graph[prev_node][node] + distance[prev_node] == distance[node]:
                stack.append(prev_node)
                if prev_node == P:
                    return 'SAVE HIM'
    return 'GOOD BYE'
N,M,P = map(int,input().split())
graph = [{} for _ in range(N+1)]
for _ in range(M):
    x,y,d = map(int,input().split())
    graph[x][y] = d
    graph[y][x] = d

INF = float('inf')
distance = [INF for _ in range(N+1)]
distance[1] = 0
node_list = []
heapq.heappush(node_list,(0,1))

while node_list:
    cur_dis,node = heapq.heappop(node_list)
    if distance[node] < cur_dis:
        continue
    for next_node in graph[node]:
        if distance[next_node] > cur_dis + graph[node][next_node]:
            distance[next_node] = cur_dis + graph[node][next_node]

            heapq.heappush(node_list,(distance[next_node],next_node))

print(solve())
