class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t=nums.sort()
        y=[]
        for i in range(len(nums)):
            if nums[i]==target:
                y.append(i)
        return y

        
