# Enter your code here. Read input from STDIN. Print output to STDOUT
n =sorted( list(map(int,input().split())))
m = sorted(list(map(int,input().split())))
from itertools import product
lis = sorted(list(product(n,m)))
l = ' '.join('('+', '.join(map(str,tpl))+')'for tpl in lis)
print(l)
