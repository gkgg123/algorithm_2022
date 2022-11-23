a = [1,1,2,2,2,8]
k = list(map(int,input().split()))
for ind in range(6):
    a[ind] -= k[ind]
print(*a)