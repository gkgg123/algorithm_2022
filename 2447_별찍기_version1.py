import sys
def input():
    return sys.stdin.readline().rstrip()
def sol(cN,x,y):
    if cN == 1:
        return
    gap = cN//3
    for dx in range(3):
        for dy in range(3):
            sx,sy = x + dx*gap,y + dy*gap
            conV = ' ' if dx == 1 and dy == 1 else '*'
            for tx in range(sx,sx+gap):
                for ty in range(sy,sy+gap):
                    arr[tx][ty] = conV
            if conV != ' ':
                sol(cN//3,sx,sy)


N = int(input())
arr = [[' ' for _ in range(N)] for _ in range(N)]
sol(N,0,0)

for row in arr:
    print(''.join(row))