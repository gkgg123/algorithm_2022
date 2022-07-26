import sys

def input():
    return sys.stdin.readline().rstrip()
def solve(left,right,flag):
    if left>right:
        return False
    while left<right:
        if st[left] == st[right]:
            left += 1
            right -= 1
        elif flag:
            s1 = solve(left+1,right,False)
            s2 = solve(left,right-1,False)
            if s1 or s2:
                return 1
            else:
                return 2
        else:
            return False
    if flag:
        return 0
    return True
T = int(input())

for _ in range(T):
    st = input()
    print(solve(0,len(st)-1,True))
