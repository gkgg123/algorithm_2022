import sys

def input():
	return sys.stdin.readline().rstrip()

N = int(input())

dp = [0 for _ in range(N+2)]


for day in range(1,N+1):
	x,y = map(int,input().split())
	dp[day] = max(dp[day],dp[day-1])
	if x + day-1>N:
		continue
	dp[x+day] = max(dp[x+day],dp[day]+y)
print(max(dp))