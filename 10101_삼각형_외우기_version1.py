arr = [int(input()) for _ in range(3)]
if sum(arr) != 180:
	print("Error")
else:
	cnt = 0
	for k in arr:
		cnt = max(cnt, arr.count(k))
	result =  ["", "Scalene", "Isosceles","Equilateral"]
	print(result[cnt])