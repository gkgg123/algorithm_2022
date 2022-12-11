def get_primes():
    nums = [False for _ in range(1001)]
    
    for num in range(2,int(1000**0.5)+1):
        if not nums[num]:
            for t in range(2*num,1001,num):
                nums[t] = True
    prime = set()
    for num in range(2,1001):
        if not nums[num]:
            prime.add(num)
    return prime

N = int(input())

arr = list(map(int,input().split()))
primes = get_primes()
cnt = 0
for num in arr:
    if num in primes:
        cnt += 1
print(cnt)