import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

def check():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for x,y in teachers:
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    break
                if arr[nx][ny] == 'O':
                    break
                if arr[nx][ny] == 'S':
                    return False
    return True

def solve():
    for w1,w2,w3 in combinations(wall_hubo,3):
        x1,y1 = w1
        x2,y2 = w2
        x3,y3 = w3
        arr[x1][y1] = 'O'
        arr[x2][y2] = 'O'
        arr[x3][y3] = 'O'
        if check():
            return 'YES'
        arr[x1][y1] = 'X'
        arr[x2][y2] = 'X'
        arr[x3][y3] = 'X'
    return 'NO'

N = int(input())

wall_hubo = []

arr = [list(input().split()) for _ in range(N)]

teachers = []
for x in range(N):
    for y in range(N):
        if arr[x][y] =='T':
            teachers.append((x,y))
        elif arr[x][y] == 'X':
            wall_hubo.append((x,y))
print(solve())