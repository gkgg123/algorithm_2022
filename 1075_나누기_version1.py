import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
F = int(input())


for i in range(100):
    cu_N = N - (N%100) + i
    if cu_N %F == 0:
        print(str(cu_N%100).zfill(2))
        break