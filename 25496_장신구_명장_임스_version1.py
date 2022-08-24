import sys

def input():
    return sys.stdin.readline().rstrip()


P,N = map(int,input().split())

arr = list(map(int,input().split()))


arr.sort()
result = 0

while P<200:
    P += arr[result]
    result += 1

print(result)