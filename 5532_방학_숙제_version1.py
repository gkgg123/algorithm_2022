import math
def cal(x,y):
    return math.ceil(x/y)
arr = [int(input()) for _ in range(5)]

print(arr[0] - max(cal(arr[1],arr[3]),cal(arr[2],arr[4])))