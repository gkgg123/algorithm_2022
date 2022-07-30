import sys

def input():
    return sys.stdin.readline().rstrip()

def romatoDecimal(st):
    num = 0
    N = len(st)
    for ind in range(N):
        if ind == N-1:
            num += romanian[st[ind]]
        elif romanian[st[ind]] >= romanian[st[ind+1]]:
            num += romanian[st[ind]]
        else:
            num -= romanian[st[ind]]
    return num

def decimaltoRoma(num):
    temp = ''
    cnt = 0
    while num != 0:
        last = num%10
        if cnt == 0:
            number = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        elif cnt == 1:
            number = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        elif cnt == 2:
            number = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        else:
            number = ['','M','MM','MMM']
        temp = number[last] + temp
        cnt += 1
        num//=10
    return temp
romanian = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
A = romatoDecimal(input())
B = romatoDecimal(input())

print(A+B)
print(decimaltoRoma(A+B))
