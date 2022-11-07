from collections import Counter

a = Counter(input().upper())
b = list(a.values())
c = b.count(max(b))
if c == 1:
	print(a.most_common()[0][0])
else:
	print("?")