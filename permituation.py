# Enter your code here. Read input from STDIN. Print output to 
inp= input().split()
n = sorted(list(inp[0]))
n = ''.join(n)
m = int(inp[1])
from itertools import permutations
lis = list(permutations(n,m))
for i in range(len(lis)):
    print(''.join(lis[i]))

