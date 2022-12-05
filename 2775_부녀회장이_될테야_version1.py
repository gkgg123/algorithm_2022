t = int(input())

for _ in range(t):
	k = int(input())
	ho = int(input())
	arr = [i for i in range(ho+1)]
	
	for _ in range(k):
		for x in range(1,ho+1):
			arr[x] += arr[x-1]
	print(arr[-1])