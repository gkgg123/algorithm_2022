n = int(input())
dp =[1,1,3]
for ind in range(2,n+1):
	dp.append(dp[-1]+dp[-2]*2)
if n%2:
	print((dp[n]+dp[(n-1)//2])//2)
else:
	print((dp[n] + dp[n//2]+2*dp[n//2-1])//2)