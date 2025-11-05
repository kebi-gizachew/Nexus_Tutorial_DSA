class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """  
        nums.sort()
        c=0
        i,j=0,len(nums)-1
        num=deque(nums)
        while j>i:
            if num[j]+num[i]==k:
                num.popleft()
                num.pop()
                c+=1
                j-=1
            elif num[j]+num[i]>k:
                num.pop()
            else:
                num.popleft()
            j-=1
    
        return c
