import sys

def input():
    return sys.stdin.readline().rstrip()


K = int(input())
K -= 1
answer = []
t = 2

while True:
    if K%t<t//2:
        answer.append('4')
    else:
        answer.append('7')
    K -= t
    t*=2
    if K <0:
        break
answer.reverse()
print(''.join(answer))