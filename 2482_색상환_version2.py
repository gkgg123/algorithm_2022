import sys
sys.setrecursionlimit(100000)
def input():
    return sys.stdin.readline().rstrip()


def solve(n,k):
    if n/k == 2:
        return 2
    elif k == 1:
        return n
    if n/2<k:
        return 0
    if dp[n][k] == 0:
        dp[n][k] = (solve(n-1,k) + solve(n-2,k-1))%mod
    return dp[n][k]

N = int(input())
K = int(input())
mod = 1000000003

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
print(solve(N,K))