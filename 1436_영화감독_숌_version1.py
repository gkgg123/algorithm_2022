N = int(input())
cnt = 0
st = 666
while True:
    if '666' in str(st):
        cnt += 1
        if cnt == N:
            break
    st += 1
print(st)