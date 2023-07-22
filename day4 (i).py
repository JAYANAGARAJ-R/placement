a=input()
c=input()
b=sorted(a.lower())
d=sorted(c.lower())
e=0
for i in range(0,len(b)):
    if len(b)==len(d):
        if b[i]==d[i]:
            e+=1
if e==len(b):
    print("YES")
else:
    print("NO")
    
        
