import sys
from collections import defaultdict,deque
def input():
    return sys.stdin.readline().rstrip()

def cha(k : str):
    if k.isupper():
        return ord(k) - ord('A')
    else:
        return ord(k)-ord('a')+26


def solve():
    st = 0
    ed = 25
    answer = 0
    while True:
        prev_node = [-1 for _ in range(52)]
        prev_node[st] = st
        queue = deque()
        queue.append(st)
        while queue and prev_node[ed] == -1:
            cur_node = queue.popleft()
            for next_node in graph[cur_node]:
                if graph[cur_node][next_node] - flow[cur_node][next_node] > 0 and prev_node[next_node] == -1:
                    prev_node[next_node] = cur_node
                    queue.append(next_node)
        if prev_node[ed] == -1:
            return answer
        min_value = float('inf')
        p = ed
        while p != st:
            min_value = min(graph[prev_node[p]][p] - flow[prev_node[p]][p] , min_value)
            p = prev_node[p]
        p = ed
        while p != st:
            flow[prev_node[p]][p] += min_value
            flow[p][prev_node[p]] -= min_value
            p = prev_node[p]
        answer += min_value

N = int(input())
graph = [defaultdict(int) for _ in range(52)]
flow  = [[0 for _ in range(52)] for _ in range(52)]
for _ in range(N):
    x,y,k = input().split()
    x,y,k = cha(x),cha(y),int(k)
    graph[x][y] += k
    graph[y][x] += k


print(solve())