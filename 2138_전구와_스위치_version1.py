import sys
def input():
    return sys.stdin.readline().rstrip()

def change(idx):
    for ii in [idx-1,idx,idx+1]:
        cs[ii] = (cs[ii]+1)%2
N = int(input())
current = [0]+list(map(int,list(input()))) + [0]
ends = [0]+list(map(int,list(input()))) + [0]
answer = float('inf')
for k in range(2):
    cs = current[:]
    cnt = 0
    for i in range(1,N+1):
        if k == 0 and i == 1:
            change(i)
            cnt += 1
        if i>1:
            if cs[i-1] != ends[i-1]:
                change(i)
                cnt += 1
    if cs[1:-1] == ends[1:-1]:
        answer = min(answer,cnt)

print(answer if answer != float('inf') else -1)