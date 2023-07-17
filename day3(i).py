def Largesmallsum(arr):
    c=[]
    d=[]
    a=len(arr)
    if a==0:
        return 0
    elif a<3:
        return 0
    else:
        for i in range(0,len(arr)):
            if i%2==1:
                c.append(arr[i])
            elif i%2==0:
                d.append(arr[i])
        c.sort()
        d.sort()
        e=c[1]+d[len(d)-2]
        return e
        
arr=list(map(int,input().split()))
print(Largesmallsum(arr))
