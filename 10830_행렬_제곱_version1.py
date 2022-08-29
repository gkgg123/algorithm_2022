import sys

def input():
    return sys.stdin.readline().rstrip()

def multi(X,Y):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for k in range(N):
                temp[x][y] += X[x][k] * Y[k][y]
            temp[x][y] %= 1000
    return temp
def solve(B):
    if B == 1:
        return arr
    half_arr = solve(B//2)
    if B%2:
        return multi(multi(half_arr,half_arr),arr)
    else:
        return multi(half_arr,half_arr)

N,B = map(int,input().split())

arr = [list(map(lambda x : x%1000,map(int,input().split()))) for _ in range(N)]


answer = solve(B)
for row in answer:
    print(*row)