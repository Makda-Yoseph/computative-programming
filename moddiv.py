# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
tup = divmod(a,b)
for i in range(len(tup)):
    print(tup[i])

print(tup)

