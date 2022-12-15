for _ in range(3):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    if sum(arr)<0:
        print("-")
    elif sum(arr):
        print("+")
    else:
        print(0)