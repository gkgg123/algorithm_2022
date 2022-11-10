def k():
    return int(input())
a = k()
b = k()
c = k()
ans = str(a*b*c)
for i in range(10):
    print(ans.count(str(i)))