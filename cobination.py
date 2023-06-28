# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input().split()
m = sorted(list(inp[0]))
n = int(inp[1])
from itertools import combinations
lis= []
for i in range(1,n+1):
    lis.append(list(combinations(m,i)))

    
for j in range(len(lis)):
    for c in range(len(lis[j])):
        print(''.join(lis[j][c]))
