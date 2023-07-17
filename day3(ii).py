def Productsmallpair(sum,arr):
    n=len(arr)
    if n<2:
        return -1
    elif n==0:
        return 0
    else:
        arr.sort()
        j=arr[0]
        k=arr[1]
        x=j+k
        if x<sum:
            return j*k
sum=int(input())

arr=list(map(int,input().split()))
print(Productsmallpair(sum,arr))    
