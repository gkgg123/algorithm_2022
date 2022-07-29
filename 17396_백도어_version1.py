import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def solve():
    heap = []
    INF = float('inf')
    heapq.heappush(heap,(0,0))
    distance_list = [INF for _ in range(N)]
    distance_list[0] = 0
    while heap:
        cur_dis,node = heapq.heappop(heap)
        if node == N-1:
            return cur_dis
        if distance_list[node] < cur_dis:
            continue
        for next_node,next_dis in graph[node]:
            if distance_list[next_node] > cur_dis + next_dis:
                distance_list[next_node] = cur_dis + next_dis
                heapq.heappush(heap,(distance_list[next_node],next_node))

    return -1

N, M = map(int,input().split())
visible = list(map(int,input().split()))

graph = [[] for _ in range(N)]
visible[-1] = 0
for _ in range(M):
    x,y,t = map(int,input().split())
    if visible[x]+visible[y] == 0:
        graph[x].append((y,t))
        graph[y].append((x,t))

print(solve())