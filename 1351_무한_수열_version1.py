import sys
def input():
    return sys.stdin.readline().rstrip()

def solve(num):
    if num == 0:
        return 1
    if dp.get(num):
        return dp[num]
    dp[num] = solve(num//P) + solve(num//Q)
    return dp[num]

N,P,Q = map(int,input().split())


dp = {}

print(solve(N))
