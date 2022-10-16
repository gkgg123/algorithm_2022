import sys
def input():
    return sys.stdin.readline().rstrip()



arr = list(map(int,input().split()))
k = list(set(arr))
if len(k) == 3:
    print(max(arr)*100)
elif len(k) == 2:
    for num in range(1,7):
        if arr.count(num) == 2:
            print(1000+num*100)
else:
    print(10000+k[0]*1000)