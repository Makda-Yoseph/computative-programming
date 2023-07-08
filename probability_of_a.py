# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
alpha=list(input().split())
k = int(input())
from itertools import combinations
lis = list(combinations(alpha,k))
count = 0
for i in range(len(lis)):
    if 'a' in lis[i]:
        count+=1

j = len(lis)
print(count/j)
    
