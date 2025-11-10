class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l=0
        s=sum(nums[:k])
        avr=s/float(k)
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[l]
            l+=1
            avr=max(avr,s/float(k))
        return avr
