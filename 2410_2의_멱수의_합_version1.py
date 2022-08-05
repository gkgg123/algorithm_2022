import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = 1

k = 0
while 2**k<=N:
    num = 2**k

    for i in range(N-num+1):
        if dp[i]:
            dp[i+num] = (dp[i] + dp[i+num])%1000000000

    k += 1

print(dp[N])