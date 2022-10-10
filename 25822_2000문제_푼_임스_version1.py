import sys

def input():
    return sys.stdin.readline().rstrip()


coin = float(input())
N = int(input())
arr = list(map(int,input().split()))
max_coin = min(coin//0.99,2)
cur_coin = 0
left = 0
right = 0
strick = 0
while right<N:
    if arr[right]:
        right += 1
    elif max_coin>cur_coin:
        cur_coin += 1
        right += 1
    else:
        left += 1
        cur_coin -= not bool(arr[left])  
    strick = max(strick,right-left)
print(strick)
print(max(arr))