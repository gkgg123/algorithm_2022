import sys
from collections import deque
def input():
	return sys.stdin.readline().rstrip()
	
N,K = map(int,input().split())
queue = deque()
name_cnt = [0 for _ in range(21)]
answer = 0
for _ in range(N):
	name = input()
	
	queue.append(len(name))
	name_cnt[len(name)] += 1
	if len(queue) > K:
		cur = queue.popleft()
		name_cnt[cur] -= 1
		answer += name_cnt[cur]
		
while queue:
		cur = queue.popleft()
		name_cnt[cur] -= 1
		answer += name_cnt[cur]

print(answer)