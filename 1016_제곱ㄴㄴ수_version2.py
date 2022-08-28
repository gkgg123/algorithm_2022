import sys

def input():
    return sys.stdin.readline().rstrip()


x,y = map(int,input().split())

sq = 2
visit = [1 for _ in range(y-x+1)]
answer = y-x+1
while sq*sq <=y:
    square = sq*sq
    mod = x//square

    while mod*square<=y:
        idx = square*mod - x
        if idx>=0 and visit[idx]:
            answer -= 1
            visit[idx] = 0
        mod += 1
    sq += 1
print(answer)