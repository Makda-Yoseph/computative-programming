# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees,atan2
ab = float(input())
bc = float(input())
ac = pow(pow(ab,2)+pow(bc,2),0.5)
ach = ac/2
d = pow(pow(bc,2)+pow(ach,2),0.5)
t = round(degrees(atan2(ab, bc)))
print(u'{}\N{DEGREE SIGN}'.format(t))


