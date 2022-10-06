import sys

def input():
    return sys.stdin.readline().rstrip()


A,B = input().split()
p = len(A[A.index('.')+1:])
upper = str(int(A.replace('.',''))**int(B))
lower = str((10**p)**int(B))
position = len(upper) - len(lower) +1
if position >=0:
    print(upper[:position] + '.' + upper[position:])
else:
    print('0.'+'0'*(-position)+upper)