import sys

def input():
    return sys.stdin.readline().rstrip()

def reverse(x,y):
    for cx in range(x,x+3):
        for cy in range(y,y+3):
            A[cx][cy] = (A[cx][cy]+1)%2

def check():
    for x in range(N):
        for y in range(M):
            if A[x][y] != B[x][y]:
                return False
    return True
N,M = map(int,input().split())

A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]
cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            reverse(i,j)
            cnt += 1

print(cnt if check() else -1)