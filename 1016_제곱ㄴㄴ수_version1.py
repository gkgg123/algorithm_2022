import sys


def input():
    return sys.stdin.readline().rstrip()


def check(y):
    square = []
    for num in range(2,int(y**0.5)+1):
        if num*num <=y:
            square.append(num*num)
    return square


x,y = map(int,input().split())

squares = check(y)
visit = [1 for _ in range(y-x+1)]

for squar in squares:
    st = x//squar
    if x%squar:
        st += 1
    for n in range(st,y//squar+1):
        if x<=n *squar <=y:
            visit[n*squar-x] = 0

print(sum(visit))