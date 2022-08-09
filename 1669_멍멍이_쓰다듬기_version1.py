import sys

def input():
    return sys.stdin.readline().rstrip()

def sol(x,y):
    gap = y-x

    n = 0
    while True:
        if n**2<=gap<(n+1)**2:
            break
        n += 1
    if n:
        day = 2*n-1
        gap -= n**2
        while gap>0:
            if gap >= n:
                gap -= n
                day += 1
            else:
                n -= 1
        return day

    else:
        return 0
a,b = map(int,input().split())
print(sol(a,b))