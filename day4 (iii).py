def calculate(a,b):
    c=[]
    for i in range(a+1,b+1):
        if i%3==0 and i%5==0:
            c.append(i)
    print(sum(c))        
a=int(input())
b=int(input())
calculate(a,b)
