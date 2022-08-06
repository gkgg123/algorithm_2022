import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def solve():
    visit = set()

    visit.add(s)
    queue = deque()
    queue.append((s,[]))
    operation = ['*','+','/']
    if s == t:
        return 0
    if t == 1:
        return '/'
    while queue:
        cs,val = queue.popleft()
        for idx,ns in enumerate([cs*cs,cs+cs]):
            if ns not in visit:
                if not (0<=ns<=1000000000): continue
                queue.append((ns,val+[operation[idx]]))
                visit.add(ns)
                if ns == t:
                    return ''.join(val+[operation[idx]])
        if cs:
            ns = cs//cs
            if ns not in visit:
                queue.append((ns,val+['/']))
                visit.add(ns)
    return -1
s,t = map(int,input().split())


print(solve())