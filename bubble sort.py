a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        else:
            continue
print(a)        
