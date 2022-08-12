import sys

def input():
    return sys.stdin.readline().rstrip()


N,R,C = map(int,input().split())

answer = 0

while N:
    N -= 1
    size = 2**N

    if R<size and C<size:
        answer += 0
    elif R<size and C>=size:
        answer += size*size
        C -= size
    elif R>=size and C<size:
        answer += size*size*2
        R -= size
    else:
        answer += size*size*3
        R -= size
        C -= size


print(answer)