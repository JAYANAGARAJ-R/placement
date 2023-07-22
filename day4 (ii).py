a=input()
b=input()
c=input()
for i in range(0,len(a)):
    if a[i]==b:
        print(c,end="")
    elif a[i]==c:
        print(b,end="")
    else:
        print(a[i],end="")
