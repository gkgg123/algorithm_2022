import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]

prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]


for i in range(N):
    for j in range(N):
        prefix_sum[i+1][j+1] = arr[i][j] + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]


answer = -float('inf')

for size in range(1,N+1):
    for x in range(size-1,N):
        for y in range(size-1,N):
            answer = max(answer, prefix_sum[x+1][y+1] - prefix_sum[x+1-size][y+1] - prefix_sum[x+1][y+1-size] + prefix_sum[x+1-size][y+1-size])

print(answer)