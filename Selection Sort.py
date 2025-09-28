class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            u=i
            for j in range(i+1,len(arr)):
                if arr[u]>arr[j]:
                    u=j
            arr[i],arr[u]=arr[u],arr[i]
        return arr
                    
                    
        #code here
