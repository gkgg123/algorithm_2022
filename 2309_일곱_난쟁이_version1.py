from itertools import combinations

def solve():
    for a in combinations(arr,7):
        if sum(a) == 100:
            b = sorted(list(a))
            b = list(map(str,b))
            return '\n'.join(b)


arr = [int(input()) for _ in range(9)]

print(solve())