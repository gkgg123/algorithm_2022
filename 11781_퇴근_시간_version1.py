import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def cal(l,cur_time,flag):
    if flag:
        if cur_time>=E or cur_time + l <= S:
            return l
        elif S<= cur_time<E:
            delay = (E - cur_time)/2
            if l<=delay:
                return l*2
            return delay*2 + (l-delay)
        elif cur_time <S:
            bd = S - cur_time
            delay = (E-S)/2
            if l <= bd  + delay:
                return bd + ((l-bd)*2)
            else:
                return delay + l
    else:
        return l

def solve():
    INF = float('inf')
    distance = [INF for _ in range(N+1)]
    node_list = []
    distance[1] = 0
    distance[0] = 0
    heapq.heappush(node_list,(0,1))
    result = 0
    while node_list:
        cur_dis,cur_node = heapq.heappop(node_list)

        if cur_dis>distance[cur_node]:
            continue
        if result<cur_dis:
            result = cur_dis
        for val  in graph[cur_node]:
            next_node,term = val
            flag = check[cur_node][next_node]
            next_dis = cur_dis + cal(term,cur_dis,flag)
            if distance[next_node]>next_dis:
                distance[next_node] = next_dis
                heapq.heappush(node_list,(distance[next_node],next_node))
    if int(result) == result:
        return int(result)
    return result
N,M,S,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
check = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y,l,t1,t2 = map(int,input().split())
    graph[x].append([y,l])
    graph[y].append([x,l])
    check[x][y] = t1
    check[y][x] = t2


print(solve())