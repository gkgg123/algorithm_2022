import sys

def input():
    return sys.stdin.readline().rstrip()

def possible(st):
    global cnt
    on = set()
    for col in range(st,st+3):
        for row in range(5):
            if Ev[row][col] == '#':
                on.add(3*row+(col-st))
    result = []
    for num in range(10):
        if on - check[num]:
            continue
        result.append(num)
    cnt *= len(result)
    return result

def solve(digit,cnt):
    if not cnt:
        return -1
    total = 0
    for idx in range(N):
        sq = N-idx-1
        times = cnt//len(digit[idx])
        total = total + (sum(digit[idx]))*(10**sq)*times
    return total/cnt
        


N = int(input())

Ev = [list(input()) for _ in range(5)]


check = [set() for _ in range(10)]
check[0].update([0,1,2,3,5,6,8,9,11,12,13,14])
check[1].update([2,5,8,11,14])
check[2].update([0,1,2,5,6,7,8,9,12,13,14])
check[3].update([0,1,2,5,6,7,8,11,12,13,14])
check[4].update([0,2,3,5,6,7,8,11,14])
check[5].update([0,1,2,3,6,7,8,11,12,13,14])
check[6].update([0,1,2,3,6,7,8,9,11,12,13,14])
check[7].update([0,1,2,5,8,11,14])
check[8].update([0,1,2,3,5,6,7,8,9,11,12,13,14])
check[9].update([0,1,2,3,5,6,7,8,11,12,13,14])

digit = [[] for _ in range(N)]
cnt = 1
for idx in range(N):
    st = 4*idx
    digit[idx].extend(possible(st))

print(solve(digit,cnt))