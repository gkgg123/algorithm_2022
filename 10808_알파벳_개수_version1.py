a = [0]*26
s = input()
k = ord('a')
for t in s:
    a[ord(t)-k] +=1
print(*a)
    