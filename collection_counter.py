# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter as ctr

n = input()
size_count= ctr(map(int,input().split()))
total = 0
for i in range(int(input())):
    (need,price)=tuple(map(int,input().split()))
    if size_count.get(need,0):
        total += price
        size_count[need] -=1
    

print(total)
