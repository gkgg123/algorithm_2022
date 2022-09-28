import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

dices = [list(map(int,input().split())) for _ in range(N)]
# 0,5
# 1,3
# 2,4
result = 0
revesre = [5,3,4,1,2,0]
total_num = set(range(1,7))
for pick_num in range(1,7):
    cnt = 0
    for dice in dices:
        revese_num = dice[revesre[dice.index(pick_num)]]
        if pick_num + revese_num == 11:
            cnt += 4
        elif pick_num == 6 or revese_num == 6:
            cnt += 5
        else:
            cnt += 6
        pick_num = revese_num
    result = max(cnt,result)
print(result)
