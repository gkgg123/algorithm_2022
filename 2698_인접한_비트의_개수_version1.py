import sys

def input():
    return sys.stdin.readline().rstrip()




T = int(input())

dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
dp[1][0][0] = 1
dp[1][0][1] = 1


for n in range(2,101):
    for k in range(0,100):
        dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]
        dp[n][k][1] = dp[n-1][k][0]
        if k:
            dp[n][k][1] += dp[n-1][k-1][1]



for _ in range(T):
    n,k = map(int,input().split())
    print(sum(dp[n][k]))