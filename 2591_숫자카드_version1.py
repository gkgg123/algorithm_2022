import sys


def input():
    return sys.stdin.readline().rstrip()


N = input()
ls = len(N)
dp = [0 for _ in range(ls)]
if ls == 1:
    print(1)
else:
    dp[0] = 1
    st = int(N[:2])
    if 10<=st<=34 and N[1] != '0':
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2, ls):
        if N[i] == '0':
            if 10<=int(N[i-1:i+1])<=34:
                dp[i] += dp[i-2]
        else:
            dp[i] += dp[i-1]
            if 10<=int(N[i-1:i+1])<=34:
                dp[i] += dp[i-2]
    print(dp[-1])