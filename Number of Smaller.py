k,l=map(int,input().strip().split())
arr1=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
i=0
arr=[]
for j in range(l):
    while  i<k and arr2[j]>arr1[i]:
        i+=1
    arr.append(i)
print(" ".join(map(str, arr)))
