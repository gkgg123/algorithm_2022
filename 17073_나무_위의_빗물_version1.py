import sys

def input():
    return sys.stdin.readline().rstrip()
N,W = map(int,input().split())
tree = [0 for _ in range(N+1)]
cnt = set()
for _ in range(N-1):
    x,y = map(int,input().split())
    tree[x] += 1
    tree[y] += 1
    if tree[x]>1 and x>1:
        cnt.add(x)
    if tree[y]>1 and y>1:
        cnt.add(y)

print(W/(N-1-len(cnt)))