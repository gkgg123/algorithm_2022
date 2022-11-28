import sys
from collections import defaultdict, deque
import heapq
def input():
    return sys.stdin.readline().rstrip()


N,L = 5000000,5000000

cnt = defaultdict(int)
arr = list(map(int,input().split()))
result = []
queue = deque()
for idx in range(N):
    while queue and queue[-1][0] > arr[idx]:
        queue.pop()
    while queue and queue[0][1] < idx - L +1:
        queue.popleft()
    queue.append((arr[idx],idx))
    result.append(queue[0][0])
print(*result)