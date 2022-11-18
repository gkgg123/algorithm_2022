def solve(a,b):
    cnt = 0
    if len(a) == len(b):
        n = len(a)
        for i in range(n):
            if a[i] == b[i] == "8":
                cnt += 1
            elif a[i] != b[i]:
                return cnt
    return cnt



a,b = input().split()



print(solve(a,b))