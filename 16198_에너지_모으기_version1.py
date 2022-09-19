import sys
def input():
    return sys.stdin.readline().rstrip()

def solve(k):
    if len(k) == 2:
        return 0
    temp = 0
    for ind in range(1,len(k)-1):
        next_arr = k[:ind] + k[ind+1:]
        a,c = k[ind-1],k[ind+1]
        temp = max(temp,a*c+solve(next_arr))
    return temp


N = int(input())
ws = list(map(int,input().split()))
print(solve(ws))
