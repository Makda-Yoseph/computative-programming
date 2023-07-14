# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
student = namedtuple('student',input().split())
total=0
for i in range(n):
    sts=student(*(input().split()))
    total += int(sts.MARKS)
print(f"{total/n:.2f}")
