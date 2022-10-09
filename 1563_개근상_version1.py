answer = []
for N in range(1,1001):
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(N+1)]

    dp[0][0][0] = 1
    M = 1000000

    for day in range(N):
        for lated in range(2):
            for back in range(3):
                dp[day+1][0][lated] += dp[day][back][lated]%M
                if lated<1:
                    dp[day+1][0][lated+1] += dp[day][back][lated]%M
                if back<2:
                    dp[day+1][back+1][lated] +=  dp[day][back][lated]%M
    result = sum(dp[N][0]) + sum(dp[N][1]) + sum(dp[N][2])
    answer.append(result%M)
print(answer)