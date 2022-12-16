n = int(input())

for _ in range(n):
	cnt = 1
	rs = 0
	for k in input():
		if k =="O":
			rs += cnt
			cnt += 1
		else:
			cnt = 1
	print(rs)