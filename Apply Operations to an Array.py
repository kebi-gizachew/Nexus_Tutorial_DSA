class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        arr=[r for r in nums if r!=0]
        arr+=[0]*(len(nums)-len(arr))
        return arr
