n=int(input().strip())
for i in range(n):
    t=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    value=True
    for k in range(1,t):
        if arr[k]-arr[k-1]>1:
            value=False
            break
    if value==True:
        print("YES")
    else:
        print("NO") 
