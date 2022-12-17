n = int(input())
k = 1
while True:
    if n<=k*(k+1)//2:
        break
    k += 1
total = k+1
remain = n - (k-1)*k//2
if k%2:
    print(f'{total-remain}/{remain}')
else:
    print(f'{remain}/{total-remain}')
 