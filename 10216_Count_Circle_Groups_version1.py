import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parents(x,make_set):
    if make_set[x] == x:
        return x
    make_set[x] = find_parents(make_set[x],make_set)
    return make_set[x]

def union(x,y,make_set):
    X = find_parents(x,make_set)
    Y = find_parents(y,make_set)
    if X<Y:
        make_set[Y] = make_set[X]
    else:
        make_set[X] = make_set[Y]            

def solve():
    N = int(input())
    nodes = []
    make_set = [i for i in range(N)]
    nodes = [list(map(int,input().split())) for _ in range(N)]

    for a1 in range(N-1):
        for a2 in range(a1+1,N):
            x1,y1,r1 = nodes[a1]
            x2,y2,r2 = nodes[a2]
            if (x1-x2)**2  + (y1-y2)**2 <= (r1+r2)**2:
                if find_parents(a1,make_set) == find_parents(a2,make_set):continue
                union(a1,a2,make_set)
    ans = 0
    for ind in range(N):
        if find_parents(ind,make_set) == ind:
            ans += 1
    print(ans)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()