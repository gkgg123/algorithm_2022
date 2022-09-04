import sys
def input():
    return sys.stdin.readline().rstrip()


def find_parent(x):
    if make_set[x] == x:
        return x
    make_set[x] = find_parent(make_set[x])
    return make_set[x]

def union(x,y):
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        return False
    if ranks[X] < ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X
    if ranks[X] == ranks[Y]:
        ranks[X] += 1
    return True
while True:
    N,M = map(int,input().split())
    if not N+M:
        break
    node_list = []
    result = 0
    for _ in range(M):
        x,y,z = map(int,input().split())
        node_list.append((z,x,y))
        result += z

    node_list.sort(key= lambda x : (-x[0]))
    make_set = [i for i in range(N)]
    ranks = [1 for _ in range(N)]
    cnt = 0
    while node_list:
        z,x,y = node_list.pop()
        if union(x,y):
            result -= z
            cnt += 1
            if cnt == N-1:
                break
    print(result)
