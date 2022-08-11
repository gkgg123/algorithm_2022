import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N = int(input())
    cafe = []
    x_val = defaultdict(list)
    for _ in range(N):
        x,y = map(int,input().split())
        x_val[x].append(y)
    prev = -1

    for x in sorted(x_val.keys()):
        x_val[x].sort()

        if prev != -1 and x_val[prev][-1] != x_val[x][0]:
            x_val[x].reverse()
        elif prev == -1:
            if x_val[0][0] != 0:
                x_val[x].reverse()
        for y in x_val[x]:
            cafe.append((x,y))
        prev = x
    _,*bunhos = list(map(int,input().split()))
    for bunho in bunhos:
        print(*cafe[bunho-1])

