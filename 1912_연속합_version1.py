import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))
result = [arr[0]]

for i in range(1,N):
    result.append(max(result[-1]+arr[i],arr[i]))

print(max(result))