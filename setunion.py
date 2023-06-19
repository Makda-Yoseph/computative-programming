# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
erol = set(input().split())
f = int(input())
frol = set(input().split())
un=erol.union(frol)
print(len(un))
