class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=sorted(nums)
        p={}
        for i,val in enumerate(d):
            if val not in p:
                p[val]=i
        return [p[x] for x in nums]
            
            




        
