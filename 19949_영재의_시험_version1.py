import sys

def input():
    return sys.stdin.readline().rstrip()



arr = list(map(int,input().split()))


stack = []

for i in range(1,6):
    if arr[0] == i:
        stack.append((1,1,i,1))
    else:
        stack.append((0,1,i,1))
result = 0
while stack:
    cor,tot,num,cnt = stack.pop()
    if 10-tot + cor < 5:
        continue
    if tot == 10:
        if cor >= 5:
            result += 1
        continue
    for i in range(1,6):
        if num == i and cnt<2:
            stack.append((cor+ int(arr[tot] == num),tot+1,num,cnt+1))
        elif num != i:
            stack.append((cor + int(i == arr[tot]),tot+1,i,1))

print(result)
