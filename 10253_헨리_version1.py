import sys
from math import ceil,gcd
def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    x,y = map(int,input().split())

    while x != 1:
        k = ceil(y/x)
        x = x*k-y
        y = y*k
        mod = gcd(x,y)
        x//=mod
        y//=mod
    print(y)