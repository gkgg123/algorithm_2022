import sys
from collections import deque
def input():
	return sys.stdin.readline().rstrip()
	
	
m,n = map(int,input().split())

arr = [list(input()) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = [0,0]

visited = [[True for _ in range(m)] for _ in range(n)]
for x in range(n):
	for y in range(m):
		if visited[x][y]:
			visited[x][y] = False
			queue = deque()
			queue.append((x,y))
			cnt = 1
			while queue:
				cx,cy = queue.popleft()
				
				
				for i in range(4):
					nx = cx + dx[i]
					ny = cy + dy[i]
					if 0<=nx<n and 0<=ny<m:
						if visited[nx][ny] and arr[nx][ny] == arr[x][y]:
							queue.append((nx,ny))
							cnt += 1
							visited[nx][ny] = False
			if arr[x][y] == 'B':
				result[1] += (cnt*cnt)
			else:
				result[0] += (cnt*cnt)
				
print(*result)
			