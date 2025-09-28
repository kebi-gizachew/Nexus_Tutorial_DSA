class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p={}
        for i in range(len(nums)):
            p[nums[i]]=p.get(nums[i],0)+1
        n=0
        for m in range(3):
            for t in range(p.get(m,0)):
                nums[n]=m
                n+=1





            
