import sys

def input():
	return sys.stdin.readline().rstrip()

t = int(input())


for _ in range(t):
	n = int(input())
	
	arr = list(map(int,input().split()))
	ans = 0
	arr.sort()
	for ind in range(2,n):
		ans = max(ans,arr[ind]-arr[ind-2])
	print(ans)