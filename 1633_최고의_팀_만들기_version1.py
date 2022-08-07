import sys


def input():
    return sys.stdin.readline().rstrip()
arr = []
while True:
    try:
        white,black = map(int,input().split())
        arr.append((white,black))
    except:
        break

N = len(arr)
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(N)]


dp[0][1][0] = arr[0][0]
dp[0][0][1] = arr[0][1]

for ind in range(1,N):
    for w in range(16):
        for b in range(16):
            white,black = arr[ind]
            dp[ind][w][b] = max(dp[ind-1][w][b],dp[ind][w][b])
            if w>0:
                dp[ind][w][b] = max(dp[ind][w][b],dp[ind-1][w-1][b]+white)
            if b>0:
                dp[ind][w][b] = max(dp[ind][w][b],dp[ind-1][w][b-1]+black)


print(dp[N-1][15][15])