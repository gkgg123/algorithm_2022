import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
INF = float('inf')
arr = list(map(int,input().split()))
dp = [[INF for _ in range(N)] for _ in range(N)]


for left in range(N-1,-1,-1):
    for right in range(left,N):
        if left == right:
            dp[left][right] = 0
        elif left +1 == right and arr[left] == arr[right]:
            dp[left+1][right+1] = 0
        else:
            if arr[left] == arr[right]:
                dp[left][right] = dp[left+1][right-1]
            dp[left][right] = min(dp[left][right] , 1 + min(dp[left+1][right] , dp[left][right-1]))
print(dp[0][N-1])