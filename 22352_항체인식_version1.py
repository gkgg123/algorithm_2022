import sys

def input():
	return sys.stdin.readline().rstrip()
	
	
N,M = map(int,input().split())

prev = [list(map(int,input().split())) for _ in range(N)]

cur = [list(map(int,input().split())) for _ in range(N)]
visit =[[0 for _ in range(M)] for _ in range(N)]
dx = [-1,0,1,0]
dy =[0,-1,0,1]
cnt = 0
for x in range(N):
	if cnt:
		break
	for y in range(M):
		if prev[x][y] != cur[x][y] and visit[x][y] ==0:
			ori = prev[x][y]
			prev[x][y] = cur[x][y]
			stack = [(x,y)]
			visit[x][y] = 1
			while stack:
				cx,cy = stack.pop()
				
				for i in range(4):
					nx = cx + dx[i]
					ny = cy + dy[i]
					if 0<=nx<N and 0<=ny<M:
						if visit[nx][ny] == 0 and prev[nx][ny] == ori:
							visit[nx][ny] = 1
							prev[nx][ny] = cur[x][y]
							stack.append((nx,ny))
			cnt += 1
			if cnt:
				break
			
			

			
flag = True
for x in range(N):
	for y in range(M):
		if prev[x][y] == cur[x][y]:
			continue
		else:
			flag = False
			break
if flag:
	print("YES")
else:
	print("NO")
	
	
		
		
