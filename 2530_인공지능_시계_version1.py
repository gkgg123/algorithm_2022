arr = list(map(int,input().split()))

time = int(input())

h = time//3600
time = time%3600
m = time//60
t = time%60
arr[0] +=h
arr[1] +=m
arr[2] +=t
arr[1] += arr[2]//60
arr[2] %=60
arr[0] += arr[1]//60
arr[1] %=60
arr[0] %=24
print(*arr)

