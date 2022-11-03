import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    two_sum = set()

    for x in range(N):
        for y in range(x,N):
            two_sum.add(arr[x]+arr[y])

    for k in range(N-1,-1,-1):
        for z in range(k):
            if arr[k] - arr[z] in two_sum:
                return arr[k]

    
N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()
print(solve())
