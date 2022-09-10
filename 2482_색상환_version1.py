import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
mod = 1000000003


dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = i
    dp[i][0] = 1

for n in range(2,N+1):
    for k in range(2,K+1):
        dp[n][k] = (dp[n-2][k-1] + dp[n-1][k])%mod

answer = dp[N-1][K] + dp[N-3][K-1]
print(answer)