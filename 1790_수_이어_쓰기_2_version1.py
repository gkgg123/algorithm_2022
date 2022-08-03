import sys

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())


digit = 1
digitOfCount = 9

while K>digit*digitOfCount:
    K -= digit*digitOfCount
    digit += 1
    digitOfCount *= 10
nums = (K-1)//digit + 10**(digit-1)
if nums >N:
    print(-1)
else:
    print(str(nums)[(K-1)%digit])