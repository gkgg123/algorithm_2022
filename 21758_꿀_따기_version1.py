from re import A
import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = [0]+list(map(int,input().split()))
prefix_sum =[0 for _ in range(N+1)]


for i in range(1,N+1):
    prefix_sum[i] =arr[i] +  prefix_sum[i-1]


answer = 0

for i in range(2,N):
    answer = max(answer,2*prefix_sum[N] - arr[i] - arr[1]-prefix_sum[i], prefix_sum[i-1] + prefix_sum[N-1] - arr[i],prefix_sum[i] - arr[1] + prefix_sum[N-1] - prefix_sum[i-1]) 
 

print(answer)