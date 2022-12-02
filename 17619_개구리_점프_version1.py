import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parents(x):
    if make_set[x] == x:
        return x
    make_set[x] = find_parents(make_set[x])
    return make_set[x]

def union(a,b):
    A = find_parents(a)
    B = find_parents(b)
    if A != B:
        if ranks[A] < ranks[B]:
            A,B = B,A
        make_set[B] = A
        if ranks[A] == ranks[B]:
            ranks[A] += 1
N,Q = map(int,input().split())

tree = []

for idx in range(N):
    x1,x2,y = map(int,input().split())
    tree.append((x1,x2,idx))

tree.sort()
s,e,pidx = tree[0]
make_set = [i for i in range(N)]
ranks = [1 for _ in range(N)]
for idx in range(1,N):
    ns,ne,nidx = tree[idx]
    if ns<=e:
        union(pidx,nidx)
        e = max(e,ne)
    else:
        s,e = ns,ne
    pidx = nidx


for idx in range(N):
    find_parents(idx)
result = []

for _ in range(Q):
    x,y = map(int,input().split())
    result.append(str(int(make_set[x-1] == make_set[y-1])))
sys.stdout.write('\n'.join(result))