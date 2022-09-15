n = int(input())

arr = list(map(int,input().split()))
k = max(arr)
result = list(map(lambda x : x/k*100,arr))
print(sum(result)/n)