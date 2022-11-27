n = int(input())
x = 0
for _ in range(n):
    x += 1 if int(input()[2:])<=90 else 0
print(x)