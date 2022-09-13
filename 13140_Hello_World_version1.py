import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()
def solve():
    for pickNums in permutations(range(10),len(keyword)):
        if pickNums[2] == 0 or pickNums[-1] == 0:
            continue
        hello = pickNums[2]*10000 + pickNums[1]*1000 + pickNums[3]*100 + pickNums[3]*10 + pickNums[4]
        world = pickNums[-1]*10000 + pickNums[4]*1000 + pickNums[-2]*100 + pickNums[3]*10 + pickNums[0]
        if hello + world == N:
            result = ['  '+str(hello), '+ '+str(world),'-------',str(N).rjust(7,' ')] 
            return '\n'.join(result)
    return 'No Answer'

N = int(input())

keyword = ['d', 'e', 'h', 'l', 'o', 'r', 'w']
print(solve())