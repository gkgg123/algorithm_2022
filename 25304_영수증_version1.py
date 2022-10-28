a = int(input())

n = int(input())
s = 0
for _ in range(n):
    x,y = map(int,input().split())
    s = s + x*y
if a == s:
    print('Yes')
else:
    print('No')