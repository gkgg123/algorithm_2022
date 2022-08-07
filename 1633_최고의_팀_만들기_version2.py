import sys

def input():
    return sys.stdin.readline().rstrip()


N = 15

dp = [[0 for _ in range(16)] for _ in range(16)]


for val in sys.stdin:
    white,black = map(int,val.split())

    for w in range(N,-1,-1):
        for b in range(N,-1,-1):
            if w > 0:
                dp[w][b] = max(dp[w][b] , dp[w-1][b] + white)
            if b > 0:
                dp[w][b] = max(dp[w][b], dp[w][b-1] + black)

print(dp[N][N])