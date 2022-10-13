from collections import deque


def solve():
	queue = deque()
	queue.append((0,n))
	visit = set()
	visit.add(n)
	ma = 99999
	while queue:
		cnt,x = queue.popleft()
		if cnt>t:
			return 'ANG'
		if x == g:
			return cnt

		if x+1 not in visit and x+1<=ma:
			queue.append((cnt+1,x+1))
			visit.add(x+1)
		
		
		if 2*x<=ma:
			nx = 2*x
			kk = 1
			while nx//kk:
				kk*=10
			kk//=10
			nx -= kk
			if nx not in visit:
				queue.append((cnt+1,nx))
				visit.add(nx)
	return "ANG"




n,t,g = map(int,input().split())


print(solve())