n,k = map(int,input().split())
result = [i for i in range(10001)]

arr = {}

for _ in range(n):
	x,y,z = map(int,input().split())
	if arr.get(x):
		arr[x].append((y,z))
	else:
		arr[x] =[(y,z)]

for d in range(k+1):
	if d>0:
		result[d] = min(result[d],result[d-1]+1)
	if arr.get(d):
		for ed,vl in arr[d]:
			result[ed] = min(result[ed],result[d]+vl)
			
print(result[k])