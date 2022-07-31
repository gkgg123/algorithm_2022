import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]


for left in range(N-1,-1,-1):
    for right in range(N-1,-1,-1):
        if B[right] < A[left]:
            dp[left][right] = dp[left][right+1] + B[right]
        else:
            dp[left][right] = max(dp[left+1][right+1],dp[left+1][right])

print(dp[0][0])