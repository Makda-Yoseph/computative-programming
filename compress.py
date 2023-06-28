# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
lis = list(m)
count = 1
newlis = []
for i in range(len(lis)):
    if i+1 < len(lis) and  lis[i]== lis[i+1]:
        count += 1
        
       
    else :
        newlis.append((count,lis[i]))
        count =1
   
print( ' '.join('('+', '.join(map(str,tpl))+')'for tpl in newlis))
        
