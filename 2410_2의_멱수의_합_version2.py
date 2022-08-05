import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
N//=2
dp = [0 for _ in range(N+1)]
dp[0] = 1
for i in range(1,N+1):
    dp[i] = (dp[i-1] + dp[i//2])%1000000000

print(dp[N])