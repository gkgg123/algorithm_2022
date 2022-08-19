import sys
def input():
    return sys.stdin.readline().rstrip()

def fibo(x):
    if x== 0:
        return [1,0]
    if x == 1:
        return [0,1]
    if visit[x]:
        return dp[x]
    a = fibo(x-1)
    b = fibo(x-2)
    visit[x] = True
    dp[x][0] = a[0] + b[0]
    dp[x][1] = a[1] + b[1]
    return dp[x]

T = int(input())

for _ in range(T):
    N = int(input())
    visit = [False for _ in range(N+1)]
    dp = [[0,0] for _ in range(N+1)]
    print(*fibo(N)) 	