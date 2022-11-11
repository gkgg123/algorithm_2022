n = int(input())
arr = list(map(int,input().split()))
result = 0
arr.sort()
for num in arr:
    if result+1<num:
        break
    result += num
print(result+1)