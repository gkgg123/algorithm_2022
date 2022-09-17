import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))


arr.sort()
answer = 0

for i in range(N):
    search = arr[:i] + arr[i+1:]
    st = 0
    ed = N-2
    while st<ed:
        temp = search[st] + search[ed]
        if temp == arr[i]:
            answer += 1
            break
        elif temp < arr[i]:
            st += 1
        else:
            ed -= 1
print(answer)