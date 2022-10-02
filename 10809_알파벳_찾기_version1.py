import sys

def input():
    return sys.stdin.readline().rstrip()


S = input()
alpha = [-1 for _ in range(26)]

for ind,t in enumerate(S):
    k = ord(t) - ord('a')
    if alpha[k] == -1:
        alpha[k] = ind
print(*alpha)