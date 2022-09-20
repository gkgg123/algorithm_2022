n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


dp[0][0] = 1

for x in range(n):
	for y in range(n):
		if arr[x][y]:
			nx = x
			ny = y + arr[x][y]
			if ny<n:
				dp[nx][ny] += dp[x][y]
				
			nx = x + arr[x][y]
			if nx<n:
				dp[nx][y] += dp[x][y]
				
				
print(dp[n-1][n-1])