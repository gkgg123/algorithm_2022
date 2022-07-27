import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    cnt = 0
    while True:
        if sum(arr) == 0:
            return cnt
        for i in range(N):
            if arr[i]%2:
                arr[i] -= 1
                break
        else:
            for i in range(N):
                arr[i]//=2
        cnt += 1
    


N = int(input())

arr = list(map(int,input().split()))


print(solve())