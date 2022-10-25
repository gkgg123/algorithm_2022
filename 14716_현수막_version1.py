import sys
from collections import deque
def input():
	return sys.stdin.readline().rstrip()
	
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
visit = set()

for x in range(n):
	for y in range(m):
		if arr[x][y] and (x,y) not in visit:
			visit.add((x,y))
			cnt += 1
			queue = deque()
			queue.append((x,y))
			while queue:
				cx,cy = queue.popleft()
				
				for i in range(8):
					nx = cx + dx[i]
					ny = cy + dy[i]
					if 0<=nx<n and 0<=ny<m:
						if (nx,ny) not in visit and arr[nx][ny]:
							visit.add((nx,ny))
							queue.append((nx,ny))
print(cnt)