import sys

def input():
    return sys.stdin.readline().rstrip()

result = []
def solve(cnt,A,B,C):
    if cnt == 1:
        result.append(f'{A} {C}')
    else:
        solve(cnt-1,A,C,B)
        result.append(f'{A} {C}')
        solve(cnt-1,B,A,C)

N = int(input())
visit = {}
print(2**N-1)
solve(N,1,2,3)
sys.stdout.write('\n'.join(result))