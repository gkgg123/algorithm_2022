import sys
from collections import Counter

def input():
	return sys.stdin.readline().rstrip()
print = sys.stdout.write
def solve(n):
	result = set()
	for nn in range(1, int(n**0.5)+1):
		if n%nn:
			continue
		result.add(nn)
		result.add(n//nn)
	total = -1
	for nnn in result:
		total += cc[nnn]
	used[n] = total
	return total
		
	
N = int(input())

arr = [int(input()) for _ in range(N)]

cc = Counter(arr)

used = {}


for num in arr:
	if used.get(num) :
		print(str(used[num])+ "\n")
	else:
		print(str(solve(num)) + "\n")