import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [int(input()) for _ in range(N)]

left = 0
right = 0 

now = arr[left]
total = sum(arr)
answer = 0
while left<=right and right<N:

    cur_min = min(total-now,now)
    answer = max(cur_min,answer)

    if cur_min == now:
        right += 1
        if right == N:
            break
        now += arr[right]
    else:
        now -= arr[left]
        left += 1
print(answer)
